#!/usr/bin/python3.6

import os
import random
import string
from flask import Flask, request
from flask_restx import Api, Resource

from texts import *

app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse2)


@api.route('/hints')
class hints(Resource):
    @api.doc(responses={200: 'Ok'})
    def get(self):
        return course2_hints


@api.route('/question1')
class question1(Resource):
    def get(self):
        return question2_1


@api.route('/question2')
class question2(Resource):
    def get(self):
        return question2_2


@api.route('/question3')
class Question3(Resource):
    def get(self):
        return question2_3


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Some users had issues on Mac with debug=True, in this case try debug=False
    app.run(debug=True, host='0.0.0.0', port=port)
