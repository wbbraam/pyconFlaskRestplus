import os

from flask import Flask
from flask_restplus import Api, Resource
from werkzeug.contrib.fixers import ProxyFix

from texts import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title=mainTitle, description=descriptiveTextCourse1)


my_name = 'Wietse'
question1_template = 'My name is {0}!'


@api.route('/myname')
class Question1(Resource):

    @staticmethod
    def get(self, name):
        return question1_template.format(my_name)


@api.route('/mynameUppercase')
class Question2(Resource):
    @staticmethod
    def get():
        return question1_template.format(my_name).upper()


@api.route('/concattedStrings')
class Question3(Resource):
    @staticmethod
    def get():
        return question1_template.format(my_name) + question1_template.format(my_name).upper()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=5000)











