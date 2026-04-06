from app.modules.BaseStatistics import BaseStatistics


class MmseStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        res = []
        result = ''
        for questionnaire_response in original_data:
            extension = questionnaire_response.get('extension')
            if extension is None or extension == [] or len(extension) != 1:
                continue

            mmse_score = extension[0]['valueInteger']
            if mmse_score >= 26:
                result = 'Normal/No Cognitive Impairment'
                res += {
                    'id': questionnaire_response.get('id'),
                    'score': mmse_score,
                    'result': result,
                },
            elif mmse_score >= 22:
                result = 'Mild Cognitive Impairment (MCI)'
                res += {
                    'id': questionnaire_response.get('id'),
                    'score': mmse_score,
                    'result': '',
                },
            else:
                result = 'Mild Dementia/Moderate Dementia/Severe Dementia'
                res += {
                    'id': questionnaire_response.get('id'),
                    'score': mmse_score,
                    'result': result,
                },

        return res
