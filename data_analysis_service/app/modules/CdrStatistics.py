from app.modules.BaseStatistics import BaseStatistics


class CdrStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        res = []
        cdr_mapping_score = {
            '0': 'No Dementia',
            '0.5': 'Questionable/Very Mild',
            '1': 'Mild',
            '2': 'Moderate',
            '3': 'Severe',
            '4': 'Profound',
            '5': 'Terminal',
        }
        for questionnaire_response in original_data:
            items = questionnaire_response.get('item')
            if items is None or items == []:
                continue

            for item in items:
                if item['linkId'] == 'CDR-Total':
                    cdr_total_score = item['answer'][0]['valueInteger']
                res += {
                    'id': questionnaire_response.get('id'),
                    'score': cdr_total_score,
                    'result': cdr_mapping_score.get(str(cdr_total_score)),
                },

        return res
