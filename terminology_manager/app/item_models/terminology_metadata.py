from typing import Dict
from pydantic import BaseModel


class TerminologyMetadata(BaseModel):
    version: str
    name: str
    created: str
    filename: str

class UpdateTerminologyMetadata(BaseModel):
    version: str
    name: str
    created: str
    filename: str
    new_version: str
    new_name: str
    new_created: str
    new_filename: str

class CodeSystemPayloadModel(BaseModel):
    resource: Dict
