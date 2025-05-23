from typing import Dict
from pydantic import BaseModel


class Track13ForPatientModel(BaseModel):
    patient_payload: Dict

class Track13ForPractitionerModel(BaseModel):
    practitioner_payload: Dict

class Track13ForGoalModel(BaseModel):
    goal_payload: Dict

class Track13ForCarePlanModel(BaseModel):
    care_plan_payload: Dict

class Track13ForConditionModel(BaseModel):
    condition_payload: Dict
    condition_type: str

class Track13ForServiceRequestModel(BaseModel):
    service_request_payload: Dict

class Track13ForObservationModel(BaseModel):
    observation_payload: Dict
