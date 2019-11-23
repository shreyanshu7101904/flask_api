from flask import Flask
import sys
from apis.signup.signup import signup
from apis.login.login import login
from apis.testapi.test_api import test


app = Flask(__name__)
app.register_blueprint(signup)
app.register_blueprint(login)
app.register_blueprint(test)

@app.route('/')
def hello_world():
    return 'test-api'

if __name__ == '__main__':
    # app.run(debug = True, host = '0.0.0.0')
    app.run(debug = True, port= 4000)