#!/usr/bin/python3.6

import string
import random
import os

from flask import Flask
from flask import request
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description='Description')

awesomeDictionaryToReturn = {}
awesomeDictionaryToReturn["Most awesome programming language."] = "Python"
awesomeDictionaryToReturn["Reason"]                             = "You dont need a reason."
awesomeDictionaryToReturn["Why"]                                = "Just try to do these labs in another language."
awesomeDictionaryToReturn["Original request"]                   = ""


@app.route('/question1')
class question1(Resource):
    def get(self):
        return ("Well you know how to create a basic api. Now lets retreive and return json shall we. Create an api that jsonifies the awesomeDictionaryToReturn to json and return it.<BR> USE THE IMPORTED JSON LIBRARY!")


@app.route('/quesiton2')
class question2(Resource):
    def get(self):
        return ("Now we got that working, why dont you retreive json from the request body and add it to the empty paramger in the dict, before returning it")


# Hint? Try google. I think you should be able to do it by adding just a few lines and that includes the app.route and def statements.
# or: https://docs.python.org/2/library/json.html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)