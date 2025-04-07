import importlib
from app.item_models.original_payload import OriginalPayload
from app.modules import ConverterService

from fastapi.responses import JSONResponse


async def convert_to_fhir(item: OriginalPayload):
    status_code = 200
    item_dict = item.model_dump()
    module_name = item_dict['module_name']
    original_data = item_dict['original_data']

    try:
        status_code = 200
        module_package = importlib.import_module(f'app.modules.{module_name}')
        module_object = getattr(module_package, module_name)
        converter_service = ConverterService.ConverterService(module_object)
        converted_result = converter_service.converter.convert(original_data)

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
