#!/usr/bin/python3.6

import os
import random
import string
from flask import Flask, request
from flask_restx import Api, Resource, fields

from texts import *

app = Flask(__name__)
api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse3)

awesomeDictionaryToReturn = {}
awesomeDictionaryToReturn["Most awesome programming language."] = "Python"
awesomeDictionaryToReturn["Reason"] = "You dont need a reason."
awesomeDictionaryToReturn["Why"] = "Just try to do these labs in another language."
awesomeDictionaryToReturn["Original request"] = ""


@api.route('/hints')
class hints(Resource):
    @api.doc(responses={200: 'Ok'})
    def get(self):
        return course3_hints


@api.route('/question1')
class question1(Resource):
    def get(self):
        return question3_1

    def post(self):
        return question3_1


@api.route('/question2')
class question2(Resource):
    def get(self):
        return question3_2


@api.route('/question3')
class question3(Resource):
    def get(self):
        return question3_3


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Some users had issues on Mac with debug=True, in this case try debug=False
    app.run(debug=True, host='0.0.0.0', port=port)
