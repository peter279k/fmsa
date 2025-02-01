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
        ig_collection.insert_one(item_dict)

        return True

    def upload_ig(zip_file):
        file_name = zip_file.filename
        file_size = len(zip_file)

        contents = zip_file.file.read()
        with open(f'/tmp/{file_name}', 'wb') as f:
            f.write(contents)

        return {
            'filename': file_name,
            'filesize': file_size,
            'filepath': f'/tmp/{file_name}',
        }
