import sys
from flask import request, Blueprint

sys.path.append('../../')
from lib.tokens.AuthTokens import jwtTokenVerify


test = Blueprint('test_login', __name__)


@test.route('/v1/user/test_login', methods=['POST'])
def test_route():
    request_json = request.get_json()
    key = request.headers.get('Token')
    val = request.headers.get('secret_key')
    print(dict(request.headers), key, "\n", val)
    if key and val:
        token_satus, val = jwtTokenVerify(val, key)
        if token_satus:
            response = {
                "message": " user validated",
                "token": key
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
