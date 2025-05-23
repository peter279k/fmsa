from urllib.parse import urlencode

from app.modules import ProfileManager
from app.item_models.profile_metadata import *

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def retrieve_profile(request: Request):
    status_code = 200
    allowed_params = ['version', 'name', 'created']
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
        profile_manager = ProfileManager.ProfileManager()
        result = profile_manager.retrieve_info(params)
        profile_manager.mongo_client.close()
    except Exception as e:
        profile_manager.mongo_client.close()
        status_code = 500

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
            'message': 'Retrieving specific Profile is successful.',
            'data': [result],
        },
        status_code=status_code
    )

async def create_profile_metadata(item: ProfileMetadata):
    status_code = 200
    item_dict = item.model_dump()
    try:
        profile_manager = ProfileManager.ProfileManager()
        result = profile_manager.create_metadata(item_dict)
        profile_manager.mongo_client.close()
    except Exception as e:
        status_code = 500
        profile_manager.mongo_client.close()

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
            'message': 'Creating specific Profile metadata is successful.',
            'data': [item.model_dump(), {'inserted_id': result}],
        },
        status_code=status_code
    )

async def upload_profile(item: ProfileStructureDefinition):
    status_code = 200
    item_dict = item.model_dump()
    try:
        profile_manager = ProfileManager.ProfileManager()
        http_response = profile_manager.upload_profile(item_dict)
        message = 'Uploading specific Profile is successful.'
        result = http_response.json()
        if http_response.status_code != 200 and http_response.status_code != 201:
            message = 'Uploading specific Profile is failed'

        profile_manager.mongo_client.close()

    except Exception as e:
        status_code = 500
        profile_manager.mongo_client.close()

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
            'status': http_response.status_code,
            'message': message,
            'data': [{'result': result}],
        },
        status_code=http_response.status_code
    )

async def update_profile(item: ProfileStructureDefinition):
    status_code = 200
    item_dict = item.model_dump()
    try:
        profile_manager = ProfileManager.ProfileManager()
        http_response = profile_manager.update_profile(item_dict)
        message = 'Updating specific Profile is successful.'
        result = http_response.json()
        if http_response.status_code != 200 and http_response.status_code != 201:
            message = 'Updating specific Profile is failed'

        profile_manager.mongo_client.close()

    except Exception as e:
        status_code = 500
        profile_manager.mongo_client.close()

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
            'status': http_response.status_code,
            'message': message,
            'data': [{'result': result}],
        },
        status_code=http_response.status_code
    )

async def retrieve_profile_from_fhir_server(request: Request):
    status_code = 200
    allowed_params = ['_id']
    item_dict = {}
    for allowed_param in allowed_params:
        if request.query_params.get(allowed_param):
            item_dict[allowed_param] = request.query_params.get(allowed_param)

    if item_dict == {}:
        status_code = 400

        return JSONResponse(
            {
                'status': status_code,
                'message': 'Retrieving specific profiles with these allowed params: {}'.format(','.join(allowed_params)),
                'data': [dict(request.query_params)],
            },
            status_code=status_code
        )

    try:
        profile_manager = ProfileManager.ProfileManager()
        http_response = profile_manager.retrieve_profile(urlencode(item_dict))
        message = 'Retrieving specific Profile is successful.'
        result = http_response.json()
        if http_response.status_code != 200 and http_response.status_code != 201:
            message = 'Retrieving specific Profile is failed'

        profile_manager.mongo_client.close()

    except Exception as e:
        status_code = 500
        profile_manager.mongo_client.close()

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [dict(request.query_params)],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': http_response.status_code,
            'message': message,
            'data': [{'result': result}],
        },
        status_code=http_response.status_code
    )

async def update_profile_metadata(item: UpdateProfileMetadata):
    status_code = 200
    try:
        profile_manager = ProfileManager.ProfileManager()
        result = profile_manager.update_profile_metadata(item.model_dump())
        profile_manager.mongo_client.close()
    except Exception as e:
        status_code = 500
        profile_manager.mongo_client.close()

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
            'message': 'Updating specific Profile metadata is successful.',
            'data': [item.model_dump(), result],
        },
        status_code=status_code
    )

async def delete_profile_metadata(request: Request):
    status_code = 200
    allowed_params = ['version', 'name', 'created']
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
        profile_manager = ProfileManager.ProfileManager()
        result = profile_manager.delete_profile_metadata(dict(params))
        profile_manager.mongo_client.close()
    except Exception as e:
        status_code = 500
        profile_manager.mongo_client.close()

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
            'message': 'Deleting specific Profile metadata is successful.',
            'data': [params, result],
        },
        status_code=status_code
    )
