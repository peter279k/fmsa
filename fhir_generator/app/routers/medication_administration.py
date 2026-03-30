from app.item_models.ltc_tw_2025 import *
from app.modules import MedicationAdministrationLtc

from fastapi.responses import JSONResponse


async def generate_ltc_tw_medication_administration(item: MedicationAdministrationLTC):
    status_code = 200
    resource_name = 'MedicationAdministration'
    item_dict = item.model_dump()
    medication_administration_resource = {}

    try:
        medication_administration = MedicationAdministrationLtc.MedicationAdministrationLtc(resource_name, item_dict)
        medication_administration_resource = medication_administration.generate_medication_request_resource()
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
            'message': 'Creating MedicationAdministration resource for LTC is successful.',
            'data': [medication_administration_resource],
        },
        status_code=status_code
    )
