import sys
from flask import request, Blueprint, abort
from marshmallow import ValidationError
import uuid

sys.path.append('../../')
from lib.mongo.MongoDbOperations import MongoLoginModule
from lib.models.UserModel import UserSchema
from lib.mongo.config import api_key_val


def generatUserId():
    user_id = str(uuid.uuid4()).split('-')[2]
    return user_id


signup = Blueprint('signup', __name__)


@signup.route('/v1/user/signup', methods=['POST'])
def addUser():
    request_json = request.get_json()
    key = request.headers.get('secret-key')
    if key and key == api_key_val:
        try:
            x = UserSchema().load(request_json)
            data_base_ob = MongoLoginModule()
            request_json["user_id"] = request_json["user_name"][0:5] + \
                generatUserId()
            status, _id = data_base_ob.addUser(request_json)
            if status:
                response = {
                    "message":" user created",
                    "id": request_json["user_id"]
                }
                return response, 200
            else:
                response = {
                    "message": "user is alreday in database"
                }
                return response, 409
        except ValidationError as e:
            response = {
                "message": e.messages
            }
            return response, 302
    else:
        response = {
            "message": "key validation error",
            "status": 404
        }
        return response, 404
