from typing import Dict
from pydantic import BaseModel


class ObservationResourceLTC(BaseModel):
    payload: Dict

class AdverseEventResourceLTC(BaseModel):
    payload: Dict
    type: str

class LocationLTC(BaseModel):
    payload: Dict

class LocationCircuitLTC(BaseModel):
    payload: Dict
    resource_name: str

class MedicationAdministrationLTC(BaseModel):
    payload: Dict

class PatientLTC(BaseModel):
    payload: Dict
    type: str

class ProcedureLTC(BaseModel):
    payload: Dict

class QuestionnaireResponseLTC(BaseModel):
    payload: Dict

class OrganizationLTC(BaseModel):
    payload: Dict

class PractitionerLTC(BaseModel):
    payload: Dict
    type: str

class PractitionerRoleLTC(BaseModel):
    payload: Dict
