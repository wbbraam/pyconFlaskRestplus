#!/usr/bin/python3.6

import os

from flask import Flask
from flask import request
from flask import jsonify
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='flask restplus workshop', description='Description')

awesome_dictionary_to_return = {"Most awesome programming language.": "Python", "Reason": "You dont need a reason.",
                             "Why": "Just try to do these labs in another language.", "Original request": ""}

awesome_dictionary = api.model('AwesomeDictionary', {
    'Original request': fields.String(required=True, min_length=1, max_length=200, description='Original request')
})


@api.errorhandler()
@api.expect(awesome_dictionary, validate = True)
@api.route('/jsonify')
class Jsonify(Resource):
    def get(self):
        return jsonify(awesome_dictionary_to_return)

    def post(self):
        data = request.json
        awesome_dictionary_to_return["Original request"] = data["Original request"]
        return jsonify(awesome_dictionary_to_return)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)