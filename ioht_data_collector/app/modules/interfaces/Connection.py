from abc import ABC, abstractmethod


class Connector(ABC):
    @abstractmethod
    def connect(self, info: dict):
        pass

class ResponseProcessor(ABC):
    @abstractmethod
    def process(self, response: dict):
        pass
