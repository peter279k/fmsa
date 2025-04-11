import importlib
from app.item_models.data_payload import DataPayload
from app.modules import StatisticsService

from fastapi.responses import JSONResponse


async def do_analysis(item: DataPayload):
    status_code = 200
    item_dict = item.model_dump()
    module_name = item_dict['module_name']
    data = item_dict['data']
    params = item_dict['params']

    try:
        status_code = 200
        module_package = importlib.import_module(f'app.modules.{module_name}')
        module_object = getattr(module_package, module_name)
        statistics_service = StatisticsService.StatisticsService(module_object())
        analyzed_result = statistics_service.statistics(data, params)

        return JSONResponse(
            {
                'status': status_code,
                'message': f'Analyzing data with {module_name} is successful.',
                'data': [analyzed_result],
            },
            status_code=status_code
        )
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [data],
            },
            status_code=status_code
        )
