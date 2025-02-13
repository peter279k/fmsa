import os

from app.item_models.terminology_metadata import *
from app.modules import TerminologyManager

from fastapi import File, UploadFile
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse


async def retrieve_terminology(request: Request):
    status_code = 200
    allowed_params = ['version', 'name', 'created', 'filename']
    params = {}
    result = {}
    for param in allowed_params:
        if request.query_params.get(param) is not None:
            params[param] = request.query_params.get(param)

    if params == {}:
        status_code = 400

        return JSONResponse(
            {
                'status': status_code,
                'message': 'Allowed params should be {}'.format(','.join(allowed_params)),
                'data': [params],
            },
            status_code=status_code
        )

    try:
        terminology_manager = TerminologyManager.TerminologyManager()
        result = terminology_manager.retrieve_info(params)
        terminology_manager.mongo_client.close()
    except Exception as e:
        status_code = 500
        terminology_manager.mongo_client.close()

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [params],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Retrieving specific Terminology is successful.',
            'data': [result],
        },
        status_code=status_code
    )

async def create_terminology_metadata(item: TerminologyMetadata):
    status_code = 200
    item_dict = item.model_dump()
    try:
        terminology_manager = TerminologyManager.TerminologyManager()
        result = terminology_manager.create_metadata(item_dict)
        terminology_manager.mongo_client.close()
    except Exception as e:
        status_code = 500
        terminology_manager.mongo_client.close()

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [item.model_dump()],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Creating specific Terminology metadata is successful.',
            'data': [item.model_dump(), {'inserted_id': result}],
        },
        status_code=status_code
    )

async def upload_terminology(zip_file: UploadFile = File(...)):
    status_code = 200
    try:
        terminology_manager = TerminologyManager.TerminologyManager()
        result = terminology_manager.upload_terminology(zip_file)
        terminology_manager.mongo_client.close()
    except Exception as e:
        zip_file.file.close()
        status_code = 500
        terminology_manager.mongo_client.close()

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [{'filename': zip_file.filename}],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Uploading specific Terminology is successful.',
            'data': [result],
        },
        status_code=status_code
    )

async def update_terminology_metadata(item: UpdateTerminologyMetadata):
    status_code = 200
    try:
        terminology_manager = TerminologyManager.TerminologyManager()
        result = terminology_manager.update_terminology_metadata(item.model_dump())
        terminology_manager.mongo_client.close()
    except Exception as e:
        status_code = 500
        terminology_manager.mongo_client.close()

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [item.model_dump()],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Updating specific Terminology metadata is successful.',
            'data': [item.model_dump(), result],
        },
        status_code=status_code
    )

async def delete_terminology_metadata(request: Request):
    status_code = 200
    allowed_params = ['version', 'name', 'created', 'filename']
    params = {}
    result = {}
    for param in allowed_params:
        if request.query_params.get(param) is not None:
            params[param] = request.query_params.get(param)

    if params == {} or len(params.keys()) != len(allowed_params):
        status_code = 400

        return JSONResponse(
            {
                'status': status_code,
                'message': 'Allowed params should be {}'.format(','.join(allowed_params)),
                'data': [params],
            },
            status_code=status_code
        )

    try:
        terminology_manager = TerminologyManager.TerminologyManager()
        result = terminology_manager.delete_terminology_metadata(dict(params))
        terminology_manager.mongo_client.close()
    except Exception as e:
        status_code = 500
        terminology_manager.mongo_client.close()

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [params],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Deleting specific Terminology metadata is successful.',
            'data': [params, result],
        },
        status_code=status_code
    )

async def retrieve_archived_code_system(request: Request):
    zip_filename = request.query_params.get('filename', '')
    zip_filepath = '/tmp/{}'.format(zip_filename)
    status_code = 404

    if os.path.isfile(zip_filepath) is False:
        return JSONResponse(
            {
                'status': status_code,
                'message': 'The {} file is not found.'.format(zip_filepath),
                'data': [],
            },
            status_code=status_code
        )

    status_code = 200
    media_type = 'application/zip'

    return FileResponse(
        status_code=status_code,
        path=zip_filepath,
        filename=zip_filename,
        media_type=media_type,
    )
