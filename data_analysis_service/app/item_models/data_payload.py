from typing import Dict, List
from pydantic import BaseModel


class DataPayload(BaseModel):
    module_name: str
    data: List
    params: Dict
