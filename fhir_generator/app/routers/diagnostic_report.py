from app.item_models.track8_2024 import *
from app.modules import Track8ForDiagnosticReport

from fastapi.responses import JSONResponse


async def generate_track8_2024_for_diagnostic_report(item: Track8ForResource):
    status_code = 200
    resource_name = 'DiagnosticReport'
    item_dict = item.model_dump()
    diagnostic_report_resource = {}

    try:
        track8_for_diagnostic_report = Track8ForDiagnosticReport.Track8ForDiagnosticReport(resource_name, item_dict)
        diagnostic_report_resource = track8_for_diagnostic_report.generate_diagnostic_report_resource()
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
            'message': 'Creating DiagnosticReport resource for Track 8 is successful.',
            'data': [diagnostic_report_resource],
        },
        status_code=status_code
    )
