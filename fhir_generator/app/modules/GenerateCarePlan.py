import hashlib
import secrets
from fhir_data_generator import CarePlan


class GenerateCareClan:
    def __init__(self, resource_id: str = ''):
        self.encoding = 'utf-8'
        if resource_id == '':
            resource_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode(self.encoding))

        self.care_plan_class = CarePlan(resource_id)
        self.status = 'active'
        self.intent = 'plan'
        self.profile_urls = []
        self.category_coding = []
        self.description = ''
        self.subject = {'reference': ''}
        self.author = {'reference': ''}
        self.goal = []
        self.activity_progress = []
        self.activity_detail = {}
        self.note = []

    def generate(self):
        self.care_plan_class.set_profile_urls(self.profile_urls)
        self.care_plan_class.set_status(self.status)
        self.care_plan_class.set_intent(self.intent)
        self.care_plan_class.set_category_coding(self.category_coding)
        self.care_plan_class.set_description(self.description)
        self.care_plan_class.set_subject(self.subject)
        self.care_plan_class.set_author(self.author)
        self.care_plan_class.set_goal(self.goal)

        self.care_plan_class.set_activity_progress(self.activity_progress)
        self.care_plan_class.set_activity_detail(self.activity_detail)

        self.care_plan_class.set_note(self.note)

        self.care_plan_class.create()
