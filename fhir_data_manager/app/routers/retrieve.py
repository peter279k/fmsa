from app.item_models.resource import *
from app.modules import RetrieveResource

from fastapi.requests import Request
from fastapi.responses import JSONResponse


async def retrieve_resource(request: Request, resource_name: str):
    status_code = 200
    query_params = str(request.query_params)

    try:
        retrieve_resource = RetrieveResource.RetrieveResource(resource_name, query_params)
        retrieved_result = retrieve_resource.retrieve()
        return JSONResponse(
            {
                'status': retrieved_result.status_code,
                'message': f'Retrieving {resource_name} is successful.',
                'data': [retrieved_result.json()],
            },
            status_code=retrieved_result.status_code
        )
    except Exception as e:
        status_code = 500

        return JSONResponse(
            {
                'status': status_code,
                'message': str(e),
                'data': [dict(query_params)],
            },
            status_code=status_code
        )
