import importlib


class BaseConverter:
    def __init__(self, module_name: str, original_data: dict):
        self.module_prefix = 'app.modules.'
        self.module_name = module_name
        self.original_data = original_data

    def convert(self):
        module_instance = importlib.import_module(f'{self.module_prefix}{self.module_name}')
        module_instance = getattr(module_instance, self.module_name)
        converted_result = module_instance.convert(self.original_data)

        return converted_result
