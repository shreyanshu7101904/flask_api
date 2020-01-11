from lib.mongo.config import api_key_val
from lib.tokens.AuthTokens import jwtTokenCreater
from lib.models.LoginModel import LoginSchema
# from lib.mongo.TokenOperation import TokenOperation
from lib.postgres.PostgresCrud import PostgresOperation
import sys
from flask import request, Blueprint
from marshmallow import ValidationError

sys.path.append('../../')


login = Blueprint('login', __name__)


@login.route('/api/v1/user/login', methods=['POST'])
def validateUser():
    request_json = request.get_json()
    key = request.headers.get('secret_key')
    if key and key == api_key_val:
        try:
            #x = LoginSchema().load(request_json)
            data_base_ob = PostgresOperation()
            status, user_detail, data = data_base_ob.loginModule(request_json)
            if status == 1:
                token = jwtTokenCreater(user_detail["user_id"], request_json)
                # data = {
                #     "key": request_json["user_id"],
                #     "value": token
                # }
                # token_ob = TokenOperation()
                # token_ob.addToken(data)
                response = {
                    "message": " user validated",
                    "token": token,
                    "data": data
                }
                return response, 200
            elif status == 2:
                response = {
                    "message": "Failed Login"
                }
                return response, 402
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
        response = {
            "message": "key validation error"
        }
        return response, 404
