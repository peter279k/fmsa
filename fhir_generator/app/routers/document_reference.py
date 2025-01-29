from app.item_models.track8_2024 import *
from app.modules import Track8ForDocumentReference

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_document_reference(item: Track8ForResource):
    status_code = 200
    resource_name = 'DocumentReference'
    item_dict = item.model_dump()
    document_reference_resource = {}

    try:
        track8_document_reference = Track8ForDocumentReference.Track8ForDocumentReference(resource_name, item_dict)
        document_reference_resource = track8_document_reference.generate_document_reference_resource()
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
            'status': status_code,
            'message': 'Creating DocumentReference resource for Track 13 is successful.',
            'data': [document_reference_resource],
        },
        status_code=status_code
    )
