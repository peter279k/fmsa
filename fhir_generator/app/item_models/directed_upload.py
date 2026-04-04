from typing import Dict
from pydantic import BaseModel


class DirectedUploadPayload(BaseModel):
    payload: Dict
