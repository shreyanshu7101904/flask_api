from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
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
            return True, data
        except  Exception as e:
            return False, e





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

    