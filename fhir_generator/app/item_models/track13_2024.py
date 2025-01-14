from typing import Dict
from pydantic import BaseModel


class Track13ForPatientModel(BaseModel):
    patient_payload: Dict
