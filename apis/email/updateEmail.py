from lib.tokens.AuthTokens import jwtTokenVerify
from lib.postgres.PostgresCrud import PostgresOperation
import sys
from flask import request, Blueprint

sys.path.append('../../')


email_update = Blueprint('email_update', __name__)


@email_update.route('/api/v1/user/update/email', methods=['POST'])
def UpdateUserEmail():
    val = request.headers.get('Token')
    key = request.headers.get('secret_key')
    if key and val:
        token_satus, val = jwtTokenVerify(key, val)
        if token_satus:
            data_base_ob = PostgresOperation()
            status, user_detail = data_base_ob.updateEmailStatus(key)
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
