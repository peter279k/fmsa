from typing import Dict
from pydantic import BaseModel


class OriginalPayload(BaseModel):
    module_name: str
    original_data: Dict
