from typing import Dict
from pydantic import BaseModel


class DataPayload(BaseModel):
    payload: Dict
