import sys
from flask import Flask, request, Blueprint
from marshmallow import ValidationError

sys.path.append('../../')
from lib.mongo.MongoDbOperations import MongoLoginModule
from lib.mongo.TokenOperation import TokenOperation
from lib.models.LoginModel import LoginSchema
from lib.tokens.AuthTokens import jwtTokenCreater



login = Blueprint('login', __name__)

@login.route('/v1/user/login', methods = ['POST'])
def validateUser():
    request_json = request.get_json()
    key = request.headers.get('secret_key')
    if key and key == 'shreyanshu' :
        try:
            x = LoginSchema().load(request_json)
            data_base_ob = MongoLoginModule()
            status, user_detail = data_base_ob.getUserByUserId("user_id", request_json["user_id"])
            if status:
                if user_detail["auth_value"] == request_json["auth_value"]:
                    token = jwtTokenCreater(request_json["user_id"],request_json)
                    data = {
                        "key": request_json["user_id"],
                        "value": token
                    }
                    token_ob = TokenOperation()
                    token_ob.addToken(data)
                    response = {
                        "message":" user validated",
                        "token" : token
                    }
                    return response,200
                else:
                    response = {
                        "message":"Failed Login"
                    }
                    return response,402 
            else:
                response = {
                    "message": "user not registered"
                }
                return response, 402
        except ValidationError as e:
            response = {
                "message": e.messages
            }
            return response, 302
    else:
        response ={
            "message" : "key validation error"
        }
        return response, 404


