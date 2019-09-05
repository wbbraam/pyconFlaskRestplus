"""__init__ module for the solutions package"""

from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

from texts import mainTitle, descriptiveTextCourse1


MY_NAME = 'Wietse'
QUESTION1_TEMPLATE = 'My name is {0}!'
API_MODEL_COURSE3 = 'AwesomeDictionary', {
    'Original request': fields.String(required=True, min_length=1, max_length=200, description='Original request')}
awesome_dictionary_to_return = {"Most awesome programming language.": "Python",
                                "Reason": "You dont need a reason.",
                                "Why": "Just try to do these labs in another language.",
                                "Original request": ""}

course4_field_names = ['employee_id', 'name']


def create_app():
    """Function creating the Flask app"""
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app


def create_api(app, title, description):
    """Function creating the Api object of flask_restplus"""
    return Api(app, version='1.0', title=title, description=description)
