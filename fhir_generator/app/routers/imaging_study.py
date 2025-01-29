from app.item_models.track8_2024 import *
from app.modules import Track8ForImagingStudy

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_imaging_study(item: Track8ForResource):
    status_code = 200
    resource_name = 'ImagingStudy'
    item_dict = item.model_dump()
    imaging_study_resource = {}

    try:
        track8_imaging_study = Track8ForImagingStudy.Track8ForImagingStudy(resource_name, item_dict)
        imaging_study_resource = track8_imaging_study.generate_imaging_study_resource()
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
            'message': 'Creating ImagingStudy resource for Track 13 is successful.',
            'data': [imaging_study_resource],
        },
        status_code=status_code
    )
