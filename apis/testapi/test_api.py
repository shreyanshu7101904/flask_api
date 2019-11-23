import sys
from flask import Flask, request, Blueprint

sys.path.append('../../')
from lib.mongo.TokenOperation import TokenOperation
from lib.tokens.AuthTokens import jwtTokenVerify



test = Blueprint('test_login', __name__)

@test.route('/v1/user/test_login', methods = ['POST'])
def test_route():
    request_json = request.get_json()
    key = request.headers.get('Token')
    if key :
        data_base_ob = TokenOperation()
        status, user_detail = data_base_ob.getToken(key)
        print(user_detail)
        print(status, user_detail)
        if status:
            token_satus, val = jwtTokenVerify(user_detail["key"], key)
            if token_satus:
                response = {
                    "message":" user validated",
                    "token" : val
                }
                return response,200
            else:
                response = {
                    "message":"Failed token Validation"
                }
                return response,402 
        else:
            response = {
                "message": "Token not available"
            }
            return response, 402
    else:
        response ={
            "message" : "key validation error"
        }
        return response, 404


