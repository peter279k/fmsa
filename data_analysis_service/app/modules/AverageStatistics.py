import statistics
from app.modules.BaseStatistics import BaseStatistics


class AverageStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        return statistics.mean(original_data)
