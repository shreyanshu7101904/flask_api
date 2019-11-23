from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from .config import *
from datetime import datetime

class TokenOperation:

    def __init__(self):
        self.conn = MongoClient(Mongo_URL)
        self.db = self.conn[login_db]["tokens"]

    def addToken(self, data):
        data["createdAt"] = datetime.now()
        try:
            _id = self.db.insert_one(data)
            return True, _id.inserted_id
        except DuplicateKeyError as e:
            return False, e

    def getToken(self, val):
        # try:
        print(val)

        data = dict(self.db.find_one({"value":val}))
        print(data)
        return True, data
        # except TypeError:
        #     return False, "object does not exists"
