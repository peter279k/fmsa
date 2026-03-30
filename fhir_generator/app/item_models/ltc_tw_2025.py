from typing import Dict
from pydantic import BaseModel


class ObservationResourceLTC(BaseModel):
    payload: Dict

class AdverseEventResourceLTC(BaseModel):
    payload: Dict
    type: str

class LocationLTC(BaseModel):
    payload: Dict

class MedicationAdministrationLTC(BaseModel):
    payload: Dict

class PatientLTC(BaseModel):
    payload: Dict
    type: str

class ProcedureLTC(BaseModel):
    payload: Dict
