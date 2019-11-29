import sys
from flask import Flask, request, Blueprint

sys.path.append('../../')
from lib.tokens.AuthTokens import jwtTokenVerify
from lib.mongo.TeamsOperation import Teams



team = Blueprint('getTeams', __name__)


@team.route('/v1/team/getTeams', methods = ['POST'])
def test_route():
    request_json = request.get_json()
    key = request.headers.get('Token')
    val = request.headers.get('secret_key')
    if key and val :
        token_satus, val = jwtTokenVerify(val, key)
        if token_satus:
            team_ob = Teams()
            teams_list = team_ob.getAllTeams()
            response = {
                "teams": teams_list
            }

            return response,200
        else:
            response = {
                "message":"Failed token Validation"
            }
            return response,402 

    else:
        response ={
            "message" : "key validation error"
        }
        return response, 404


