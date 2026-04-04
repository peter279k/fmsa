from app.modules import DirectedUploader
from app.item_models.directed_upload import *


from fastapi.responses import JSONResponse


async def directed_uploading_resource(resource_name: str, item: DirectedUploadPayload):
    status_code = 200
    item_dict = item.model_dump()

    try:
        directed_uploader = DirectedUploader.DirectedUploader(resource_name, item_dict)
        uploaded_response = directed_uploader.upload_resource()
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [item_dict],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': uploaded_response.status_code,
            'message': f'Upload {resource_name} directly is successful.',
            'data': [item_dict['payload']],
        },
        status_code=uploaded_response.status_code
    )
