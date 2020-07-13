#!/usr/bin/python3.6

import os
import random
import string
from flask import Flask, request
from flask_restx import Api, Resource, fields

from texts import *

app = Flask(__name__)
api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse4)


@api.route('/dummy')
class question1(Resource):
    def get(self):
        return "Dummy"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Some users had issues on Mac with debug=True, in this case try debug=False
    app.run(debug=True, host='0.0.0.0', port=port)
