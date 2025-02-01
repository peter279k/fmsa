from app.item_models.ig_metadata import *
from app.modules import ImplementationGuideManager

from fastapi import File, UploadFile
from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def retrieve_ig(request: Request):
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
        ig_manager = ImplementationGuideManager.ImplementationGuideManager()
        result = ig_manager.retrieve_info(params)
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
            'message': 'Retrieving specific Implementation Guide is successful.',
            'data': [result],
        },
        status_code=status_code
    )

async def create_ig_metadata(item: ImplementationGuideMetadata):
    status_code = 200
    item_dict = item.model_dump()
    try:
        ig_manager = ImplementationGuideManager.ImplementationGuideManager()
        ig_manager.create_metadata(item_dict)
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
            'message': 'Creating specific Implementation Guide metadata is successful.',
            'data': [item.model_dump()],
        },
        status_code=status_code
    )

async def upload_ig(zip_file: UploadFile = File(...)):
    status_code = 200
    try:
        ig_manager = ImplementationGuideManager.ImplementationGuideManager()
        result = ig_manager.upload_ig(zip_file)
    except Exception as e:
        zip_file.file.close()
        status_code = 500

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
            'message': 'Uploading specific Implementation Guide is successful.',
            'data': [result],
        },
        status_code=status_code
    )
