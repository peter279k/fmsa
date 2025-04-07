from app.modules.BaseConverter import BaseConverter


class ConverterService:
    def __init__(self, converter: BaseConverter):
        self.converter = converter

    def convert(self, original_data):
        return self.converter.convert(original_data)
