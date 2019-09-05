"""Module for the solutions of course2.py"""

import os
import logging as logger

from flask import request
from flask_restplus import Resource, fields
from werkzeug.exceptions import BadRequest

from solutions import create_api, create_app
from texts import mainTitle, descriptiveTextCourse2


app = create_app() # pylint: disable=invalid-name
api = create_api(app, mainTitle, descriptiveTextCourse2) # pylint: disable=invalid-name

API_MODEL = api.model('Resource', {
    'value1': fields.Integer(required=True),
    'value2': fields.Integer(required=True)})


###################
logger.getLogger().setLevel(logger.INFO)
NAME_FIRST_PARAM = 'value1'
NAME_SECOND_PARAM = 'value2'
###################


@api.route('/sum')
class Sum(Resource):
    """Endpoint for /sum"""
    @staticmethod
    @api.doc(params={NAME_FIRST_PARAM: 'value1', NAME_SECOND_PARAM: 'value2'})
    def get():
        """GET endpoint for /sum"""
        logger.info('Calculating the sum of the params..(GET)')
        return get_param_as_int(NAME_FIRST_PARAM) + get_param_as_int(NAME_SECOND_PARAM)

    @staticmethod
    @api.expect(API_MODEL, validate=True)
    def post():
        """POST endpoint for /myname"""
        logger.info('Calculating the sum of the params..(POST)')
        data = request.json
        print(data)
        return data[NAME_FIRST_PARAM] + data[NAME_SECOND_PARAM]


@api.route('/compute/<string:action>')
class Compute(Resource):
    """Endpoint for /compute/{action}"""
    @staticmethod
    def post(action):
        """POST endpoint for /compute/{action}"""
        try:
            return calculate(action, request.form.to_dict())
        except Exception as error:
            logger.error(error)
            raise BadRequest


def calculate(action, data):
    """Function for determining the action and calculating the result"""
    try:
        first_param = int(data.get(NAME_FIRST_PARAM))
        second_param = int(data.get(NAME_SECOND_PARAM))
    except Exception:
        raise BadRequest

    if action.lower() == 'subtract':
        result = first_param - second_param
    elif action.lower() == 'multiply':
        result = first_param * second_param
    elif action.lower() == 'add':
        result = first_param + second_param
    elif action.lower() == 'divide':
        result = first_param / second_param
    else:
        logger.error('Type of calculation is wrong')
        raise BadRequest(description='Wrong type of compute. Try again..')

    return result


def get_param_as_int(param_name):
    """Function for returning the int values of parameters"""
    try:
        return int(request.args.get(param_name))
    except TypeError as error:
        logger.error(error)
        raise BadRequest(description='Parameters need to be int!')


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=PORT)
