from app.item_models.track8_2024 import *
from app.item_models.track13_2024 import *
from app.modules import Track8ForCarePlan
from app.modules import Track13ForCarePlan

from fastapi.responses import JSONResponse


async def generate_track13_2024_for_care_plan(item: Track13ForCarePlanModel):
    status_code = 200
    resource_name = 'CarePlan'
    item_dict = item.model_dump()
    care_plan_resource = {}

    try:
        track13_for_care_plan = Track13ForCarePlan.Track13ForCarePlan(resource_name, item_dict)
        care_plan_resource = track13_for_care_plan.generate_care_plan_resource()
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
            'message': 'Creating CarePlan resource for Track 13 is successful.',
            'data': [care_plan_resource],
        },
        status_code=status_code
    )

async def generate_track8_2024_for_care_plan(item: Track8ForResource):
    status_code = 200
    resource_name = 'CarePlan'
    item_dict = item.model_dump()
    care_plan_resource = {}

    try:
        track8_for_care_plan = Track8ForCarePlan.Track8ForCarePlan(resource_name, item_dict)
        care_plan_resource = track8_for_care_plan.generate_care_plan_resource()
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
            'message': 'Creating CarePlan resource for Track 8 is successful.',
            'data': [care_plan_resource],
        },
        status_code=status_code
    )
