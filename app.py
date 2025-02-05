from flask import Flask
from flask_cors import CORS
from apis.signup.signup import signup
from apis.login.login import login
from apis.teams.getAllTeams import teams
from apis.teams.getTeamsById import team_by_id
from apis.email.updateEmail import email_update
from apis.email.changeEmail import email_change
from apis.mobile.updateMobile import mobile_update
from apis.mobile.changeMobile import mobile_change
from apis.changepassword.changepassword import change_password
from apis.matches.getmatches import  get_match_data
from apis.users.addUserDetails import add_user_details
from apis.users.getUserDetails import get_user_details

app = Flask(__name__)
CORS(app)
app.register_blueprint(signup)
app.register_blueprint(login)
# app.register_blueprint(teams)
# app.register_blueprint(team_by_id)
app.register_blueprint(email_update)
app.register_blueprint(email_change)
app.register_blueprint(mobile_update)
app.register_blueprint(mobile_change)
app.register_blueprint(change_password)
app.register_blueprint(get_match_data)
app.register_blueprint(get_user_details)
app.register_blueprint(add_user_details)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug = True, port= 4000)
