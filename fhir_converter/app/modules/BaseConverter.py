from abc import ABC, abstractmethod


class BaseConverter(ABC):
    @abstractmethod
    def convert(self, original_data: list):
        pass
