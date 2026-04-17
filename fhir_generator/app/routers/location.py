import httpx
from app.item_models.track8_2024 import *
from app.item_models.ltc_tw_2025 import *
from app.modules import Track8ForLocation
from app.modules import LocationResourceLtc

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_location(item: Track8ForResource):
    status_code = 200
    resource_name = 'Location'
    item_dict = item.model_dump()
    location_resource = {}

    try:
        track8_for_location = Track8ForLocation.Track8ForLocation(resource_name, item_dict)
        location_resource = track8_for_location.generate_location_resource()
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
            'message': 'Creating Location resource for Track 8 is successful.',
            'data': [location_resource],
        },
        status_code=status_code
    )

async def generate_ltc_tw_location(item: LocationLTC):
    status_code = 200
    resource_name = 'Location'
    item_dict = item.model_dump()
    location_resource = {}

    try:
        track8_for_location = LocationResourceLtc.LocationResourceLtc(resource_name, item_dict)
        location_resource = track8_for_location.generate_location_resource()
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
            'message': 'Creating Location resource for Track 8 is successful.',
            'data': [location_resource],
        },
        status_code=status_code
    )

async def generate_ltc_tw_location_circuit(item: LocationCircuitLTC):
    status_code = 200
    resource_name = 'Location'
    item_dict = item.model_dump()
    resource_name = item_dict['resource_name']
    location_resource = {}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    try:
        track8_for_location = LocationResourceLtc.LocationResourceLtc(resource_name, item_dict)
        location_resource = track8_for_location.generate_location_resource()
        del location_resource['meta']

        response = httpx.post(
            f'http://fhir_data_manager:8000/api/v1/upload/{resource_name}',
            headers=headers,
            json={'resource': location_resource}
        )
        response.raise_for_status()
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
            'message': 'Creating/Uploading Location resource is successful.',
            'data': [location_resource],
        },
        status_code=status_code
    )
