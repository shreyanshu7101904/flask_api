from lib.tokens.AuthTokens import jwtTokenVerify
from lib.postgres.PostgresCrud import PostgresOperation
import sys
from flask import request, Blueprint

sys.path.append('../../')


change_password = Blueprint('change_password', __name__)


@change_password.route('/api/v1/user/change/password', methods=['POST'])
def UpdatePassword():
    val = request.headers.get('Token')
    key = request.headers.get('secret_key')
    response_ = request.get_json()
    if key and val:
        token_satus, val = jwtTokenVerify(key, val)  # secret_key, token
        if token_satus:
            data_base_ob = PostgresOperation()
            status, user_detail = data_base_ob.changePassword(
                key, response_['auth_value'])
            if status:
                response = {
                    "message": "details updated"
                }
                return response, 200
            else:
                response = {
                    "message": "user id doesnot exists"
                }
                return response, 402
        else:
            response = {
                "message": "Token key error"
            }
            return response, 404
    else:
        response = {
            "message": "data format error"
        }
        return response, 403
