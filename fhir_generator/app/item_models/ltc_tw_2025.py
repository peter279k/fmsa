from typing import Dict
from pydantic import BaseModel


class ObservationResourceLTC(BaseModel):
    payload: Dict
