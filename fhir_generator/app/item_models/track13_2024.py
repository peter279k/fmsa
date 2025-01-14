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
