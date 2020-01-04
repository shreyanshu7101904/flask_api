from flask import Flask
from flask_cors import CORS
from apis.signup.signup import signup
from apis.login.login import login
from apis.teams.getAllTeams import teams
from apis.teams.getTeamsById import team_by_id
from apis.email.updateEmail import email_update
from apis.mobile.updateMobile import mobile_update


app = Flask(__name__)
CORS(app)
app.register_blueprint(signup)
app.register_blueprint(login)
# app.register_blueprint(teams)
# app.register_blueprint(team_by_id)
app.register_blueprint(email_update)
app.register_blueprint(mobile_update)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug = True, port= 4000)
