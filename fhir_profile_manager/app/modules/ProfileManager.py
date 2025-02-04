import os
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
