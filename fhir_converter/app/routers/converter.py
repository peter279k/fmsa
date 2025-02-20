from app.item_models.original_payload import OriginalPayload
from app.modules import BaseConverter

from fastapi.responses import JSONResponse


async def convert_to_fhir(item: OriginalPayload):
    status_code = 200
    item_dict = item.model_dump()
    module_name = item_dict['module_name']
    original_data = item_dict['original_data']

    try:
        status_code = 200
        converter = BaseConverter.BaseConverter(module_name, original_data)
        converted_result = converter.convert()

        return JSONResponse(
            {
                'status': status_code,
                'message': f'Converting data with {module_name} is successful.',
                'data': [converted_result],
            },
            status_code=status_code
        )
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [original_data],
            },
            status_code=status_code
        )
