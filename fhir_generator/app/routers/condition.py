from app.item_models.track13_2024 import *
from app.modules import Track13ForCondition

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
