from pydantic import BaseModel


class ProfileMetadata(BaseModel):
    version: str
    name: str
    created: str
    structure_definition: str

class UpdateProfileMetadata(BaseModel):
    version: str
    name: str
    created: str
    structure_definition: str
    new_version: str
    new_name: str
    new_created: str
    new_structure_definition: str

class ProfileStructureDefinition(BaseModel):
    structure_definition: str
