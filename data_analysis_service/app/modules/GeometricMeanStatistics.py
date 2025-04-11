import statistics
from app.modules.BaseStatistics import BaseStatistics


class GeometricMeanStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        return statistics.geometric_mean(original_data)
