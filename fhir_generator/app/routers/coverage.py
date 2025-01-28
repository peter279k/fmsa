from app.item_models.track8_2024 import *
from app.modules import Track8ForCoverage

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_coverage(item: Track8ForResource):
    status_code = 200
    resource_name = 'Coverage'
    item_dict = item.model_dump()
    coverage_resource = {}

    try:
        track8_for_coverage = Track8ForCoverage.Track8ForCoverage(resource_name, item_dict)
        coverage_resource = track8_for_coverage.generate_coverage_resource()
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
            'message': 'Creating Coverage resource for Track 8 is successful.',
            'data': [coverage_resource],
        },
        status_code=status_code
    )
