from lib.tokens.AuthTokens import jwtTokenVerify
from lib.mongo.MongoDbOperations import MongoOperations
import sys
from flask import request, Blueprint
from flask import jsonify

sys.path.append('../../')


get_user_details = Blueprint('get_user_details', __name__)


@get_user_details.route('/api/v1/user/details/getuserdetails', methods=['POST'])
def getUserDetails():
    val = request.headers.get('Token')
    key = request.headers.get('secret_key')
    if key and val:
        token_satus, val = jwtTokenVerify(key, val)
        if token_satus:
            data_base_ob = MongoOperations()
            status, user_detail = data_base_ob.getUserDetails(key)
            if status:
                response = {
                    "data": jsonify(user_detail)
                }
                return response, 200
            else:
                response = {
                    "message": "unable to insert_data"
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
