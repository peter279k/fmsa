from app.item_models.track8_2024 import *
from app.modules import Track8ForClaim

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_claim(item: Track8ForResource):
    status_code = 200
    resource_name = 'Claim'
    item_dict = item.model_dump()
    claim_resource = {}

    try:
        track8_for_claim = Track8ForClaim.Track8ForClaim(resource_name, item_dict)
        claim_resource = track8_for_claim.generate_claim_resource()
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
            'message': 'Creating Claim resource for Track 8 is successful.',
            'data': [claim_resource],
        },
        status_code=status_code
    )
