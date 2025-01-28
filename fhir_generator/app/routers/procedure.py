from app.item_models.track8_2024 import *
from app.modules import Track8ForProcedure

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_procedure(item: Track8ForResource):
    status_code = 200
    resource_name = 'Procedure'
    item_dict = item.model_dump()
    procedure_resource = {}

    try:
        track8_for_procedure = Track8ForProcedure.Track8ForProcedure(resource_name, item_dict)
        procedure_resource = track8_for_procedure.generate_procedure_resource()
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
            'message': 'Creating Procedure resource for Track 8 is successful.',
            'data': [procedure_resource],
        },
        status_code=status_code
    )
