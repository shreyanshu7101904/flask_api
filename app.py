from flask import Flask
from flask_cors import CORS
import sys
from apis.signup.signup import signup
from apis.login.login import login
from apis.teams.getAllTeams import team
from apis.testapi.test_api import test


app = Flask(__name__)
CORS(app)
app.register_blueprint(signup)
app.register_blueprint(login)
app.register_blueprint(team)
app.register_blueprint(test)



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    # app.run(debug = True, port= 4000)
