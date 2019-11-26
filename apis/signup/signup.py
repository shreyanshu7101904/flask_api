import sys
from flask import Flask, request, jsonify, Blueprint, abort
from marshmallow import ValidationError
# from flask_api import status

sys.path.append('../../')
from lib.mongo.MongoDbOperations import MongoLoginModule
from lib.models.UserModel import UserSchema
from lib.mongo.config import api_key_val



signup = Blueprint('signup', __name__)

@signup.route('/v1/user/signup', methods = ['POST'])
def addUser():
    request_json = request.get_json()
    key = request.headers.get('secret_key')
    if key and key == api_key_val :
        try:
            x = UserSchema().load(request_json)
            data_base_ob = MongoLoginModule()
            status, _id = data_base_ob.addUser(request_json)
            if status:
                response = {
                    "message":" user created",
                    "id": str(_id)
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
        response ={
            "message" : "key validation error",
            "status": 404
        }
        return response


