from abc import ABC, abstractmethod


class BaseStatistics(ABC):
    @abstractmethod
    def statistics(self, original_data: list, params: dict):
        pass
