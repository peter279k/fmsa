from app.modules.BaseConverter import BaseConverter


class ConverterService:
    def __init__(self, converter: BaseConverter):
        self.converter = converter

    def converting(self, original_data: list):
        return self.converter.convert(original_data)
