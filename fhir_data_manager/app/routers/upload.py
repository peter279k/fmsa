from app.item_models.resource import *
from app.modules import UploadResource

from fastapi.responses import JSONResponse


async def upload_resource(resource_name: str, item: UploadPayloadModel):
    status_code = 200
    item_dict = item.model_dump()

    try:
        upload_resource = UploadResource.UploadResource(resource_name, item_dict)
        uploaded_result = upload_resource.upload()
        return JSONResponse(
            {
                'status': uploaded_result.status_code,
                'message': f'Uploading {resource_name} is successful.',
                'data': [uploaded_result.json()],
            },
            status_code=uploaded_result.status_code
        )
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [item_dict['resource']],
            },
            status_code=status_code
        )

async def update_resource(resource_name: str, item: UploadPayloadModel):
    status_code = 200
    item_dict = item.model_dump()

    try:
        upload_resource = UploadResource.UploadResource(resource_name, item_dict)
        uploaded_result = upload_resource.upload('PUT')
        return JSONResponse(
            {
                'status': uploaded_result.status_code,
                'message': f'Uploading {resource_name} is successful.',
                'data': [uploaded_result.json()],
            },
            status_code=uploaded_result.status_code
        )
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [item_dict['resource']],
            },
            status_code=status_code
        )

async def delete_resource(resource_name: str, resource_id: str):
    status_code = 200

    try:
        upload_resource = UploadResource.UploadResource(resource_name, {})
        deleted_result = upload_resource.delete(resource_id)
        return JSONResponse(
            {
                'status': deleted_result.status_code,
                'message': f'Uploading {resource_name} is successful.',
                'data': [deleted_result.json()],
            },
            status_code=deleted_result.status_code
        )
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [{'resource_id': resource_id}],
            },
            status_code=status_code
        )
