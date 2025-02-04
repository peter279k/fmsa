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
    except Exception as e:
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
    except Exception as e:
        status_code = 500

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
        result = {}
        if http_response.status_code != 200 and http_response.status_code != 201:
            message = http_response.status_code
            result = http_response.json()

    except Exception as e:
        status_code = 500

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
            'message': message,
            'data': [item.model_dump(), {'result': result}],
        },
        status_code=status_code
    )

async def update_profile_metadata(item: UpdateProfileMetadata):
    status_code = 200
    try:
        profile_manager = ProfileManager.ProfileManager()
        result = profile_manager.update_profile_metadata(item.model_dump())
    except Exception as e:
        status_code = 500

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
    except Exception as e:
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
            'message': 'Deleting specific Profile metadata is successful.',
            'data': [params, result],
        },
        status_code=status_code
    )
