from app.item_models.track8_2024 import *
from app.modules import Track8ForMedicationRequest

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_medication_request(item: Track8ForResource):
    status_code = 200
    resource_name = 'MedicationRequest'
    item_dict = item.model_dump()
    medication_request_resource = {}

    try:
        track8_for_medication_request = Track8ForMedicationRequest.Track8ForMedicationRequest(resource_name, item_dict)
        medication_request_resource = track8_for_medication_request.generate_medication_request_resource()
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
            'message': 'Creating MedicationRequest resource for Track 8 is successful.',
            'data': [medication_request_resource],
        },
        status_code=status_code
    )
