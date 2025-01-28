from app.item_models.track8_2024 import *
from app.modules import Track8ForPractitionerRole

from fastapi.responses import JSONResponse


async def generate_track13_2024_for_practitioner_role(item: Track8ForResource):
    status_code = 200
    resource_name = 'PractitionerRole'
    item_dict = item.model_dump()
    practitioner_role_resource = {}

    try:
        track8_for_practitioner_role = Track8ForPractitionerRole.Track8ForPractitionerRole(resource_name, item_dict)
        practitioner_role_resource = track8_for_practitioner_role.generate_practitioner_role_resource()
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
            'message': 'Creating PractitionerRole resource for Track 8 is successful.',
            'data': [practitioner_role_resource],
        },
        status_code=status_code
    )
