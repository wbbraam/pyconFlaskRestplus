"""Module for the solutions of course1.py"""

import os

from flask_restx import Resource
from solutions import create_app, create_api, MY_NAME, QUESTION1_TEMPLATE
from texts import mainTitle, descriptiveTextCourse1


app = create_app()  # pylint: disable=invalid-name
api = create_api(app, mainTitle, descriptiveTextCourse1)  # pylint: disable=invalid-name


@api.route('/myname')
class Question1(Resource):
    """Endpoint for /myname"""

    @staticmethod
    def get():
        """GET endpoint for /myname"""
        return QUESTION1_TEMPLATE.format(MY_NAME)


@api.route('/mynameUppercase')
class Question2(Resource):
    """Endpoint for /mynameUppercase"""

    @staticmethod
    def get():
        """GET endpoint for /mynameUppercase"""
        return QUESTION1_TEMPLATE.format(MY_NAME).upper()


@api.route('/concattedStrings')
class Question3(Resource):
    """Endpoint for /concattedStrings"""

    @staticmethod
    def get():
        """GET endpoint for /concattedStrings"""
        return QUESTION1_TEMPLATE.format(MY_NAME) + QUESTION1_TEMPLATE.format(MY_NAME).upper()


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=PORT)
