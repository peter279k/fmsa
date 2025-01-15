from app.item_models.track13_2024 import *
from app.modules import Track13ForGoal

from fastapi.responses import JSONResponse


async def generate_track13_2024_for_goal(item: Track13ForGoalModel):
    status_code = 200
    resource_name = 'Goal'
    item_dict = item.model_dump()
    goal_resource = {}

    try:
        track13_for_goal = Track13ForGoal.Track13ForGoal(resource_name, item_dict)
        goal_resource = track13_for_goal.generate_goal_resource()
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
            'message': 'Creating Goal resource for Track 13 is successful.',
            'data': [goal_resource],
        },
        status_code=status_code
    )
