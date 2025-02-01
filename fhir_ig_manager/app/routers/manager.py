from app.modules import ImplementationGuideManager

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def retrieve_ig(request: Request):
    status_code = 200
    allowed_params = ['version', 'name', 'created']
    params = {}
    result = {}
    for param in allowed_params:
        if request.query_params.get(param) is not None:
            params[param] = request.query_params.get(param)

    if params == {}:
        status_code = 400

        return JSONResponse(
            {
                'status': status_code,
                'message': 'Allowed params should be {}'.format(','.join(allowed_params)),
                'data': [params],
            }
        )

    try:
        ig_manager = ImplementationGuideManager.ImplementationGuideManager()
        result = ig_manager.retrieve_info(params)
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [params],
            },
            status_code=status_code
        )


    return JSONResponse(
        {
            'status': status_code,
            'message': 'Retrieving specific Implementation Guide is successful.',
            'data': [result],
        },
        status_code=status_code
    )
