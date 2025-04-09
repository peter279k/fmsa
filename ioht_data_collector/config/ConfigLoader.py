from abc import ABC, abstractmethod


class ConfigLoader(ABC):
    @abstractmethod
    def load_config(self, config_path, allowed_sections, allowed_keys):
        pass
