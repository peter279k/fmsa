import statistics
from app.modules.BaseStatistics import BaseStatistics


class MedianStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        return statistics.median(original_data)
