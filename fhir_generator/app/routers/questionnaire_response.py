from app.item_models.ltc_tw_2025 import *
from app.modules import QuestionnaireResponseResourceLtc

from fastapi.responses import JSONResponse


async def generate_ltc_tw_questionnaire_response(item: QuestionnaireResponseLTC):
    status_code = 200
    resource_name = 'QuestionnaireResponse'
    item_dict = item.model_dump()
    questionnaire_response_resource = {}

    try:
        questionnaire_response = QuestionnaireResponseResourceLtc.QuestionnaireResponseResourceLtc(resource_name, item_dict)
        questionnaire_response_resource = questionnaire_response.generate_questionnaire_response_resource()
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
            'message': 'Creating QuestionnaireResponse resource for LTC is successful.',
            'data': [questionnaire_response_resource],
        },
        status_code=status_code
    )
