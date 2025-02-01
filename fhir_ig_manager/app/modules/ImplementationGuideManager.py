import os
import pymongo


class ImplementationGuideManager:
    def __init__(self):
        self.db_username = os.getenv('FHIR_IG_MANAGER_DB_USER', '')
        self.db_password = os.getenv('FHIR_IG_MANAGER_DB_PASSWORD', '')
        self.db_name = os.getenv('FHIR_IG_MANAGER_DB', '')
        self.collection = 'ig_collections'
        self.mongo_client = pymongo.MongoClient(
            host='fhir_ig_manager_db',
            port=27017,
            username=self.db_username,
            password=self.db_password
        )

    def retrieve_info(self, params: dict):
        db = self.mongo_client[self.db_name]
        ig_collection = db[self.collection]
        result = ig_collection.find_one(params)
        if result is None:
            result = {}

        if result.get('_id'):
            result['_id'] = str(result['_id'])
        if result.get('created'):
            result['created'] = result['created'].strftime('%Y-%m-%d %H:%M:%S')

        return result

    def create_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        ig_collection = db[self.collection]
        inserted_result = ig_collection.insert_one(item_dict)

        return str(inserted_result.inserted_id)

    def upload_ig(self, zip_file):
        file_name = zip_file.filename

        contents = zip_file.file.read()
        with open(f'/tmp/{file_name}', 'wb') as f:
            file_size = f.write(contents)

        return {
            'filename': file_name,
            'filesize': file_size,
            'filepath': f'/tmp/{file_name}',
        }

    def update_ig_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        ig_collection = db[self.collection]
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

        deleted_result = ig_collection.delete_one(original_metadata)
        inserted_result = ig_collection.insert_one(new_metadata)

        if os.path.isfile(original_metadata['filename']) is True:
            os.remove(original_metadata['filename'])

        return {
            'deleted_result': deleted_result.deleted_count,
            'inserted_result': str(inserted_result.inserted_id),
        }

    def delete_ig_metadata(self, item_dict: dict):
        db = self.mongo_client[self.db_name]
        ig_collection = db[self.collection]
        original_metadata = {
            'version': item_dict['version'],
            'name': item_dict['name'],
            'created': item_dict['created'],
            'filename': item_dict['filename'],
        }

        deleted_result = ig_collection.delete_one(original_metadata)

        return {
            'deleted_result': deleted_result.deleted_count,
        }
