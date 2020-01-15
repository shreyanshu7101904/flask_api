from lib.tokens.AuthTokens import jwtTokenVerify
from lib.mongo.MongoDbOperations import MongoOperations
import sys
from flask import request, Blueprint

sys.path.append('../../')


get_match_data = Blueprint('get_match_data', __name__)


@get_match_data.route('/api/v1/matches/getmatchlist', methods=['POST'])
def GetMatchDetails():
    val = request.headers.get('Token')
    key = request.headers.get('secret_key')
    if key and val:
        token_satus, val = jwtTokenVerify(key, val)
        if token_satus:
            data_base_ob = MongoOperations()
            status, match_detail = data_base_ob.getAllMatches()
            if status:
                response = {
                    "data": match_detail
                }
                return response, 200
            else:
                response = {
                    "errror_message": match_detail
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
