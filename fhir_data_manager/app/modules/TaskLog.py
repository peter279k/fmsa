import os
import pymongo


class TaskLog:
    def __init__(self):
        self.db_username = os.getenv('FHIR_DATA_MANAGER_DB_USER', '')
        self.db_password = os.getenv('FHIR_DATA_MANAGER_DB_PASSWORD', '')
        self.db_name = os.getenv('FHIR_DATA_MANAGER_DB', '')
        self.collection = 'task_log_collections'
        self.mongo_client = pymongo.MongoClient(
            host='fhir_data_manager_db',
            port=27017,
            username=self.db_username,
            password=self.db_password
        )
        self.fhir_server_headers = {
            'Accept': 'application/fhir+json',
            'Content-Type': 'application/fhir+json',
        }

    def write_log(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        terminology_collection = db[self.collection]
        inserted_result = terminology_collection.insert_one(item_dict)

        return str(inserted_result.inserted_id)

    def get_log(self, params: dict):
        db = self.mongo_client[self.db_name]
        terminology_collection = db[self.collection]
        result = terminology_collection.find_one(params)
        if result is None:
            result = {}

        if result.get('_id'):
            result['_id'] = str(result['_id'])
        if result.get('created') and hasattr(result['created'], 'strftime'):
            result['created'] = result['created'].strftime('%Y-%m-%d %H:%M:%S')

        return result
