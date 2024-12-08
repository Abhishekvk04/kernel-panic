from pymongo import MongoClient

class AtlasClient():

    def __init__ (self, altas_uri, dbname):
        self.mongodb_client = MongoClient(altas_uri)
        self.database = self.mongodb_client[dbname]

    def ping(self):
        self.mongodb_client.admin.command('ping')

    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection

    def find(self, collection_name, filter = {}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items

    def insert_many(self, collection_name, documents):
        collection = self.database[collection_name]
        collection.insert_many(documents)

    def insert_one(self, collection_name, document):
        collection = self.database[collection_name]
        collection.insert_one(document)
