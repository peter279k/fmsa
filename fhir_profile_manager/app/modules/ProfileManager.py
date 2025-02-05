import os
import json
import httpx
import pymongo


class ProfileManager:
    def __init__(self):
        self.db_username = os.getenv('FHIR_PROFILE_MANAGER_DB_USER', '')
        self.db_password = os.getenv('FHIR_PROFILE_MANAGER_DB_PASSWORD', '')
        self.db_name = os.getenv('FHIR_PROFILE_MANAGER_DB', '')
        self.collection = 'profile_collections'
        self.mongo_client = pymongo.MongoClient(
            host='fhir_profile_manager_db',
            port=27017,
            username=self.db_username,
            password=self.db_password
        )
        self.fhir_server_headers = {
            'Accept': 'application/fhir+json',
            'Content-Type': 'application/fhir+json',
        }
        self.fhir_server = 'http://fhir-server-adapter:8080/fhir/StructureDefinition'

    def retrieve_info(self, params: dict):
        db = self.mongo_client[self.db_name]
        profile_collection = db[self.collection]
        result = profile_collection.find_one(params)
        if result is None:
            result = {}

        if result.get('_id'):
            result['_id'] = str(result['_id'])
        if result.get('created') and hasattr(result['created'], 'strftime'):
            result['created'] = result['created'].strftime('%Y-%m-%d %H:%M:%S')

        return result

    def create_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        profile_collection = db[self.collection]
        inserted_result = profile_collection.insert_one(item_dict)

        return str(inserted_result.inserted_id)

    def upload_profile(self, item_dict: dict):
        profile_json_str = item_dict['structure_definition']
        response = httpx.post(self.fhir_server, headers=self.fhir_server_headers, content=profile_json_str)

        return response

    def update_profile(self, item_dict: dict):
        profile_json_str = item_dict['structure_definition']
        profile_id = json.loads(item_dict['structure_definition_id'])['id']
        fhir_server = f'{self.fhir_server}/{profile_id}'
        response = httpx.put(fhir_server, headers=self.fhir_server_headers, content=profile_json_str)

        return response

    def retrieve_profile(self, query_params: str):
        fhir_server = f'{self.fhir_server}?{query_params}'
        response = httpx.get(fhir_server, headers=self.fhir_server_headers)

        return response

    def update_profile_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        profile_collection = db[self.collection]
        original_metadata = {
            'version': item_dict['version'],
            'name': item_dict['name'],
            'created': item_dict['created'],
            'structure_definition': item_dict['structure_definition'],
        }

        new_metadata = {
            'version': item_dict['new_version'],
            'name': item_dict['new_name'],
            'created': item_dict['new_created'],
            'structure_definition': item_dict['new_structure_definition'],
        }

        deleted_result = profile_collection.delete_one(original_metadata)
        inserted_result = profile_collection.insert_one(new_metadata)

        return {
            'deleted_result': deleted_result.deleted_count,
            'inserted_result': str(inserted_result.inserted_id),
        }

    def delete_profile_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        profile_collection = db[self.collection]
        original_metadata = dict(item_dict)
        deleted_result = profile_collection.delete_one(original_metadata)

        return {
            'deleted_result': deleted_result.deleted_count,
        }
