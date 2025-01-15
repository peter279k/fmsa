from typing import Dict
from pydantic import BaseModel


class UploadPayloadModel(BaseModel):
    resource: Dict
