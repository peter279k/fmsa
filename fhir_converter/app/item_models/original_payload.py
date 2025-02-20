from typing import List
from pydantic import BaseModel


class OriginalPayload(BaseModel):
    module_name: str
    original_data: List
