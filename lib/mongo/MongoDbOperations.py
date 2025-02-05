from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson import  json_util, objectid
import  json
from .config import *



class MongoOperations:
    
    def __init__(self):
        self.conn = MongoClient(Mongo_URL)
        self.db = self.conn[default_db]


    def getAllMatches(self):
        coll_match = self.db[matches_colection]
        try:
            data = coll_match.find({}, {'_id':0})
            final_data = []
            for i in data:
                final_data.append(i)
            return True, final_data
        except  Exception as e:
            return False, e

    def getUserDetails(self, user_id):
        user_coll = self.db['users']
        try:
            data_ = user_coll.find_one({'user_id': user_id})
            data = json.loads(json_util.dumps(data_))
            del data["_id"]
            return 1, data
        except Exception as e:
            return 0, e

    def addUserDetails(self, data):
        user_coll = self.db['users']
        try:
            data = user_coll.update({"user_id": data['user_id']},data, upsert=True)
            return 1, 'user updated'
        except Exception as e:
            return 0, e

# if __name__ == '__main__':
#     ob = MongoLoginModule()
#     test = {
#         "name":"abc",
#         "key1":"abc",
#         "key12":"shreyanshu"
#     }
#     print(ob.addUser(test))
#     print(ob.getAllUsers())
    # print(ob.getUserByUserId("abc"))

    
