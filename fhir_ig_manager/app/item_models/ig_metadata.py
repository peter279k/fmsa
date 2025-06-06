from pydantic import BaseModel


class ImplementationGuideMetadata(BaseModel):
    version: str
    name: str
    created: str
    filename: str

class UpdateImplementationGuideMetadata(BaseModel):
    version: str
    name: str
    created: str
    filename: str
    new_version: str
    new_name: str
    new_created: str
    new_filename: str
