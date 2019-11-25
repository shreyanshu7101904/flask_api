from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from .config import *



class MongoLoginModule:
    
    def __init__(self):
        self.conn = MongoClient(Mongo_URL)
        self.db = self.conn[login_db][login_collection]


    def getAllUsers(self):
        users = self.db.find()
        users_list = [i for i in users]
        return users_list

    def addUser(self, data):
        try:
            _id = self.db.insert_one(data)
            return True, _id.inserted_id
        except DuplicateKeyError as e:
            return False, e

    def getUserByUserId(self, key, val):
        try:
            data = dict(self.db.find_one({key:val}))
            return True, data
        except TypeError:
            return False, "object does not exists"

    # def updateUserData(self, key, val):
        




if __name__ == '__main__':
    ob = MongoLoginModule()
    test = {
        "name":"abc",
        "key1":"abc",
        "key12":"shreyanshu"
    }
    print(ob.addUser(test))
    print(ob.getAllUsers())
    # print(ob.getUserByUserId("abc"))

    