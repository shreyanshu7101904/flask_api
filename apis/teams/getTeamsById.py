import sys
from flask import request, Blueprint

sys.path.append('../../')
from lib.tokens.AuthTokens import jwtTokenVerify
from lib.mongo.TeamsOperation import Teams


team_by_id = Blueprint('getTeamsById', __name__)


@team_by_id.route('/v1/team/getTeamsById', methods=['POST'])
def getteambyid():
    request_json = request.get_json()
    key = request.headers.get('Token')
    val = request.headers.get('secret_key')
    if key and val:
        token_satus, val = jwtTokenVerify(val, key)
        if token_satus:
            if 'team_id' in request_json:
                team_ob = Teams()
                teams_list = team_ob.getTeamById(request_json["team_id"])
                response = {
                    "team": teams_list
                }

                return response, 200
            else:
                response = {
                    "message": "invalid data parameter"
                }
                return response, 200
        else:
            response = {
                "message": "Failed token Validation"
            }
            return response, 402

    else:
        response = {
            "message": "key validation error"
        }
        return response, 404
        