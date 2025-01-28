from typing import Dict
from pydantic import BaseModel


class Track8ForResource(BaseModel):
    payload: Dict
