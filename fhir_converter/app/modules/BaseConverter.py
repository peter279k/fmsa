from abc import ABC, abstractmethod


class BaseConverter(ABC):
    @abstractmethod
    def convert(self):
        pass
