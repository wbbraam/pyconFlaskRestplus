#This is to declutter your course source codes

mainTitle='PYCON 2019 - flask_restplus workshop'

#COURSE 1
descriptiveTextCourse1 = """
<H1>Welcome to the flask restplus workshop for the pycon2019 UK.</H1>
This short workshop will teach you some of the basics for using flask with the flask_restplus module.<BR>
The workshop consists out of a series of course*.py files ramping up in complexity. If it is all just a tad
to easy, feel free to skip over some of the questions and continue to the next course*.py file.
<H2>So how do we get started</H2>
Go to the the swagger interface (http://127.0.0.1:5000), but my guess is, you are already there
Click on default
Click on question1 (or a next question if you like)
Click try it out
Click on execute 

The last step atually calls a simple get api and returns you the first exercise in the response body field.

<H2>Topic of course1.py</H2>
Basic http get api calls and a little string manipulation.
We start of really easy
<H2> Hints / Tips </H2>
Click and try the hints api
"""

question1_1 = "Build a new api /myname supporting the http method: get. Make it return your name."
question1_2 = "Build a new api /mynameUppercase returning this string all uppercase."
question1_3 = "Build a new api /concattedStrings returning questionString concatted to questionString2"

course1_hints = """
All api endpoints start of with an @api.route annotation. So for your own question make a new endpoint

Directly following this endpoint define a new class, this class will handle all interaction with your endpoint

Within the new class declare a get method. Flask restplus will recognize this as the code to be executed if a get http call 
is made to your api endpoint. That easy, no extra declarations are needed.

Any value returned by your get method will be the data returned by your api. For now we stick to strings but,
flask restplus has some nice additional tricks for easy json creation.

"""

#COURSE 2
descriptiveTextCourse2 = """
Course file 2 leanrs you how to accept parameters in your API,
we will start with reading the parameters from the HTTP Get call.
And in the last one we will read the payload of an HTTP Post"""

question2_1 = 'Build a new api /sum accept 2 parameters called parma and parb. Add them together and return the result'
question2_2 = 'Now adjust /sum to have the parameters documented in the swagger interface'
question2_3 = 'Passing parameters in a get is not the best way. Create a post method within the /sum endpoint, and allow a HTTP Post api call'
question2_4 = 'Build an api called /compute/<string:action>/ and allow for add,subtract,multiply and divide actions'

course2_hints = """
1)
request.art.get("foobar") gives you the foobar parameter from the api url.
parameters in an url are passed like this:
http://127.0.0.1/sumfoobar?foobar1=bla&foobar2=blabla

2)
Documenting parameters can be done using the following annotation
@api.doc(params={'parmfoo': 'valuebar'})

3)
retreiving the body of a post can be done using request.data
request.json is also an option but we tackle json later on.

4)
The get method or post method should now be
def post(self, action):
and the action parameter is filled from the api end point.

"""