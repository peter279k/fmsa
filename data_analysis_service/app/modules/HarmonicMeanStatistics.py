import statistics
from app.modules.BaseStatistics import BaseStatistics


class HarmonicMeanStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        return statistics.harmonic_mean(original_data)
