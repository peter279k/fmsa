import os
import pymongo


class TerminologyManager:
    def __init__(self):
        self.db_username = os.getenv('TERMINOLOGY_MANAGER_DB_USER', '')
        self.db_password = os.getenv('TERMINOLOGY_MANAGER_DB_PASSWORD', '')
        self.db_name = os.getenv('TERMINOLOGY_MANAGER_DB', '')
        self.collection = 'terminology_collections'
        self.mongo_client = pymongo.MongoClient(
            host='terminology_manager_db',
            port=27017,
            username=self.db_username,
            password=self.db_password
        )

    def retrieve_info(self, params: dict):
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

    def create_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        terminology_collection = db[self.collection]
        inserted_result = terminology_collection.insert_one(item_dict)

        return str(inserted_result.inserted_id)

    def upload_terminology(self, contents, filename):

        with open(f'/tmp/{filename}', 'wb') as f:
            filesize = f.write(contents)

        return {
            'filename': filename,
            'filesize': len(contents),
            'filepath': f'/tmp/{filename}',
        }

    def update_terminology_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        terminology_collection = db[self.collection]
        original_metadata = {
            'version': item_dict['version'],
            'name': item_dict['name'],
            'created': item_dict['created'],
            'filename': item_dict['filename'],
        }

        new_metadata = {
            'version': item_dict['new_version'],
            'name': item_dict['new_name'],
            'created': item_dict['new_created'],
            'filename': item_dict['new_filename'],
        }

        deleted_result = terminology_collection.delete_one(original_metadata)
        inserted_result = terminology_collection.insert_one(new_metadata)

        filepath = '/tmp/{}'.format(original_metadata['filename'])
        if os.path.isfile(filepath) is True:
            os.remove(filepath)

        return {
            'deleted_result': deleted_result.deleted_count,
            'inserted_result': str(inserted_result.inserted_id),
        }

    def delete_terminology_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        terminology_collection = db[self.collection]
        original_metadata = dict(item_dict)
        deleted_result = terminology_collection.delete_one(original_metadata)

        filepath = '/tmp/{}'.format(original_metadata['filename'])
        if os.path.isfile(filepath) is True:
            os.remove(filepath)

        return {
            'deleted_result': deleted_result.deleted_count,
        }
