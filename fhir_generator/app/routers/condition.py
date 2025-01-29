from app.item_models.track8_2024 import *
from app.item_models.track13_2024 import *
from app.modules import Track8ForCondition
from app.modules import Track13ForCondition

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def generate_track13_2024_for_condition(item: Track13ForConditionModel):
    status_code = 200
    resource_name = 'Condition'
    item_dict = item.model_dump()
    condition_resource = {}

    try:
        track13_for_condition = Track13ForCondition.Track13ForCondition(resource_name, item_dict)
        condition_resource = track13_for_condition.generate_condition_resource()
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
            'message': 'Creating Condition resource for Track 13 is successful.',
            'data': [condition_resource],
        },
        status_code=status_code
    )

async def generate_track8_2024_for_condition(request: Request, item: Track8ForResource):
    status_code = 200
    resource_name = 'Condition'
    item_dict = item.model_dump()
    condition_resource = {}
    condition_type = request.query_params.get('type', '')

    try:
        track8_for_condition = Track8ForCondition.Track8ForCondition(resource_name, item_dict)
        if condition_type == 'ConditionChiefComplaint-min':
            condition_resource = track8_for_condition.generate_condition_chief_resource()
        else:
            condition_resource = track8_for_condition.generate_condition_resource()
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
            'message': 'Creating Condition resource for Track 8 is successful.',
            'data': [condition_resource],
        },
        status_code=status_code
    )
