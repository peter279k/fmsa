import statistics
from app.modules.BaseStatistics import BaseStatistics


class ModeStatistics(BaseStatistics):
    def statistics(self, original_data: list, params: dict):
        return statistics.mode(original_data)
