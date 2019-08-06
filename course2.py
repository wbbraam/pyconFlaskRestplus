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

@api.route('/about')
class about(Resource):

    def get(self):
        return ("Course chapter 2. Parameter retreival.")
    
@api.route('/question1')
@api.doc(params={'parma': 'number 1', 'parmb': 'number2'})
class question1(Resource):

    def get(self):
        parma = request.args.get("parma")
        parmb = request.args.get("parmb")
        return parma + parmb
    
       
# Hints, you can capture parameters given in the url with: target = request.args.get("parameter") 
# Thats why we have added the import request at the top.
# Now build it yourself.
#
# parameters during an "http get" in a url are given like this btw:
#
# http://www.myapiserver.com:5000/coolApi?parameter=foo&parameter2=bar

@api.route('/question2')
class question2(Resource):
    def get(self, id):
        return ("Now make sure your api is documented in swagger. add the @api.doc commands for respons and parameters")

@api.route('/question3')
class question3(Resource):

    def get(self):
        return ("Now a get to pass parameters is not the nicest way. Add a post method to your class, to also accept a post request")

    def post(self):
        return

@api.route('/question4/<string:whattodo>/')
class question4(Resource):

    def get(self, whattodo):
        print(whattodo)
        return ("Another way of getting the parameters is by using a dynamic url for your api. Check the code of question4, how the whattodo parameter is implemented. Now build an api for question 3 that allows to add, multiply, subtract etc. depending on the url.")


# Hints, use request.data to retreive the content of the put body. If you want to already try json and dicts
# try request.get_json() but we will dive into json at lab3

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

