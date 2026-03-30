from app.item_models.ltc_tw_2025 import *
from app.modules import AdverseEventResourceLtc

from fastapi.responses import JSONResponse


async def generate_ltc_tw_adverse_event(item: AdverseEventResourceLTC):
    status_code = 200
    resource_name = 'AdverseEvent'
    item_dict = item.model_dump()
    adverse_event_resource = {}

    try:
        adverse_event = AdverseEventResourceLtc.AdverseEventResourceLtc(resource_name, item_dict)
        adverse_event_resource = adverse_event.generate_adverse_event_resource()
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
            'message': 'Creating AdverseEvent resource for LTC is successful.',
            'data': [adverse_event_resource],
        },
        status_code=status_code
    )
