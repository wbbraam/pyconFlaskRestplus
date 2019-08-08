#!/usr/bin/python3.6

import os
import logging as logger

from flask import Flask
from flask import request
from flask import abort
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from werkzeug.exceptions import BadRequest

from texts import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description=descriptiveTextCourse2)

###################
port_number = 5000
logger.getLogger().setLevel(logger.INFO)
name_first_param = 'param_a'
name_second_param = 'param_b'
###################


@api.doc(params={name_first_param: 'Parameter 1', name_second_param: 'Parameter 2'})
@api.route('/sum')
class Sum(Resource):
    def get(self):
        logger.info('Calculating the sum of the params..(GET)')
        return get_param_as_int(name_first_param) + get_param_as_int(name_second_param)

    def post(self):
        logger.info('Calculating the sum of the params..(POST)')
        data = request.form
        print(data)
        return data


@api.route('/compute/<string:action>')
class Compute(Resource):
    def post(self, action):
        try:
            calculate(action, request.form)
        except Exception as error:
            logger.error(error)
            raise BadRequest


def calculate(action, data):
    first_param = data[name_first_param]
    second_param = data[name_second_param]

    if action.lower() == 'subtract':
        return first_param - second_param
    elif action.lower() == 'multiply':
        return first_param * second_param
    elif action.lower() == 'add':
        return first_param + second_param
    elif action.lower() == 'divide':
        return first_param / second_param
    else:
        logger.error('Type of calculation is wrong')
        raise BadRequest(description = 'Wrong type of compute. Try again..')


def get_param_as_int(param_name):
    try:
        return int(request.args.get(param_name))
    except ValueError as error:
        logger.error('Type of parameter need to be int!')
        raise BadRequest(description = 'Parameters need to be int!')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", port_number))
    app.run(debug=True, host='127.0.0.1', port=port)
