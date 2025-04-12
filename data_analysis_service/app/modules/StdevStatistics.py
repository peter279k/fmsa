import statistics
from app.modules.BaseStatistics import BaseStatistics


class StdevStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        xbar = None
        if params.get('xbar'):
            xbar = params['xbar']

        return statistics.stdev(original_data, xbar)
