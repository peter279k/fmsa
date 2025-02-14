import os
import uuid
import httpx
import datetime
import subprocess
from urllib.parse import urlencode

from app.item_models.resource import *
from app.modules import TaskLog
from app.modules import RetrieveResource

from fastapi import BackgroundTasks
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def retrieve_resource(request: Request, resource_name: str):
    status_code = 200
    query_params = str(request.query_params)

    try:
        retrieve_resource = RetrieveResource.RetrieveResource(resource_name, query_params)
        retrieved_result = retrieve_resource.retrieve()
        return JSONResponse(
            {
                'status': retrieved_result.status_code,
                'message': f'Retrieving {resource_name} is successful.',
                'data': [retrieved_result.json()],
            },
            status_code=retrieved_result.status_code
        )
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [dict(query_params)],
            },
            status_code=status_code
        )

async def import_archived_code_system(request: Request, background_tasks: BackgroundTasks):
    status_code = 200
    zip_filename = request.query_params.get('filename', '')
    if os.path.isfile(zip_filename) is False:
        status_code = 404
        return JSONResponse(
            {
                'status': status_code,
                'message': f'The {zip_filename} file is not found.',
                'data': [],
            },
            status_code=status_code
        )

    processed_id = uuid.uuid4().hex
    background_tasks.add_task(execute_hapi_fhir_cli_task, zip_filename, processed_id)

    return JSONResponse(
        {
            'status': status_code,
            'message': f'Importing the {zip_filename} is on the way.',
            'data': [{'processed_id': processed_id}],
        },
        status_code=status_code
    )

async def execute_hapi_fhir_cli_task(zip_filename: str, processed_id: str):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    encoded_uri = urlencode({'filename': zip_filename})
    response = httpx.get(
        f'http://terminology_manager:8000/retrieve_archived_code_system?{encoded_uri}',
        headers=headers
    )

    if response.status_code != 200:
        log_content = {
            'processed_id': processed_id,
            'created':  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'message': response.text,
            'status_code': response.status_code,
        }

        try:
            task_log = TaskLog.TaskLog()
            task_log.write_log(log_content)
        except Exception as e:
            # TODO: ELK integration
            task_log.mongo_client.close()
            pass

    check_fhir_server_process = 'ps aux | grep [h]api-fhir-cli'
    result = subprocess.run(check_fhir_server_process.split(' '), capture_output=True)
    if result.returncode > 0:
        try:
            log_content = {
                'processed_id': processed_id,
                'created':  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'message': 'Another hapi-fhir-cli process is still running.',
            }

            task_log = TaskLog.TaskLog()
            task_log.write_log(log_content)
            task_log.mongo_client.close()
        except Exception as e:
            # TODO: ELK integration
            pass

        return False

    try:
        with open(zip_filename, mode='wb') as f:
            f.write(response.content)

        command = f'/app/hapi-fhir-cli/hapi-fhir-cli upload-terminology -d /tmp/{zip_filename} -v r4 -t http://fhir-server-adapter:8080/fhir -u http://loinc.org -s 10GB'
        commands = command.split(' ')
        result = subprocess.run(commands, capture_output=True)
        log_content = {
            'processed_id': processed_id,
            'created':  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'message': result.stdout.decode('utf-8'),
            'status_code': result.returncode,
        }

        task_log = TaskLog.TaskLog()
        task_log.write_log(log_content)
        task_log.mongo_client.close()

    except Exception as e:
        # TODO: ELK integration
        task_log.mongo_client.close()
        pass

async def retrieve_code_system_log(request: Request):
    status_code = 200
    processed_id = request.query_params.get('processed_id', '')

    try:
        params = {'processed_id': processed_id}
        task_log = TaskLog.TaskLog()
        result = task_log.get_log(params)
        task_log.mongo_client.close()

        return JSONResponse(
            {
                'status': status_code,
                'message': 'Retrieve code system importing log is successful',
                'data': [result],
            },
            status_code=status_code
        )
    except Exception as e:
        # TODO: ELK integration
        task_log.mongo_client.close()
        pass
