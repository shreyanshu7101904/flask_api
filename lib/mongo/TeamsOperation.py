from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from .config import Mongo_URL, login_db, teams_collection



class Teams:
    
    def __init__(self):
        self.conn = MongoClient(Mongo_URL)
        self.db = self.conn[login_db][teams_collection]


    def getAllTeams(self):
        teams = self.db.find()
        teams_list = [i for i in teams]
        return teams_list

    def addTeam(self, data):
        try:
            _id = self.db.insert_one(data)
            return True, _id.inserted_id
        except DuplicateKeyError as e:
            return False, e

    def getTeamById(self, val):
        try:
            data = dict(self.db.find_one({"_id":val}))
            return True, data
        except TypeError:
            return False, "object does not exists"

        
    def removeTeamById(self, val):
        try:
            remove_ = self.db.delete_one({"_id":val})
            return True
        except Exception as e:
            return False



if __name__ == '__main__':
    ob = Teams()
    test = {
        "name":"abc",
        "key1":"abc",
        "key12":"shreyanshu"
    }
    # print(ob.addUser(test))
    print(ob.getAllTeams())
    # print(ob.getUserByUserId("abc"))

    