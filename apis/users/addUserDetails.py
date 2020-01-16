from lib.tokens.AuthTokens import jwtTokenVerify
from lib.mongo.MongoDbOperations import MongoOperations
import sys
from flask import request, Blueprint

sys.path.append('../../')


add_user_details = Blueprint('add_user_details', __name__)


@add_user_details.route('/api/v1/user/details/adduserdetails', methods=['POST'])
def addUserDetails():
    val = request.headers.get('Token')
    key = request.headers.get('secret_key')
    req_ob = request.get_json()
    if key and val:
        token_satus, val = jwtTokenVerify(key, val)
        if token_satus:
            data_base_ob = MongoOperations()
            req_ob['user_id'] = key
            status, user_detail = data_base_ob.addUserDetails(req_ob)
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
