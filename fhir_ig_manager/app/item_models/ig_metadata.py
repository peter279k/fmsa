from pydantic import BaseModel


class ImplementationGuideMetadata(BaseModel):
    version: str
    name: str
    created: str
    filename: str
