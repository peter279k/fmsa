from app.modules.BaseStatistics import BaseStatistics


class StatisticsService:
    def __init__(self, calculator: BaseStatistics):
        self.calculator = calculator

    def statistics(self, original_data: list, params: dict):
        return self.calculator.statistics(original_data, params)
