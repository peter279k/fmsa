from app.item_models.track8_2024 import *
from app.modules import Track8ForOrganization

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_organization(item: Track8ForResource):
    status_code = 200
    resource_name = 'Organization'
    item_dict = item.model_dump()
    organization_resource = {}

    try:
        track8_for_organization = Track8ForOrganization.Track8ForOrganization(resource_name, item_dict)
        organization_resource = track8_for_organization.generate_organization_resource()
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
            'message': 'Creating Organization resource for Track 8 is successful.',
            'data': [organization_resource],
        },
        status_code=status_code
    )
