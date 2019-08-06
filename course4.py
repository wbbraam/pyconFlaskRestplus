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

@api.route('/question1')
class question1(Resource):
    def get(self):
        return ("So lets add it all together now. Create an api with patch,post,get and delete method to alter lines in a csv file")

@api.route('/question2')
class question2(Resource):
    def get(self):
        return ("Ok now add error codes that mean something on empty file etc. Check comment below to find aborter documentation")
    #https://flask-restplus.readthedocs.io/en/stable/errors.html#

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)