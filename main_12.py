"""
This applications gives us view count (meaning, number of times the page has
been reloaded)


home_url:port_number/
home_url:port_number/date


NOTES ::

-----------------------
Model-Control-View
-----------------------
Model :: everything related to database

Control :: business logic

View :: front-end

------------------------------------
#################################

------------------------------------
Model-Template-View
------------------------------------

Model :: database related stuff
Template :: front-end
View :: business logic

    - class-based view
    - function-based view

"""

from datetime import datetime
from flask import Flask

app = Flask(__name__)

counter = 0

# app.route decorator  is used to bind a function to specific URL route
@app.route("/")
def welcome():
    return "Welcome to our application"


@app.route("/date")
def date():
    return f"This page is served at {str(datetime.now())}"


@app.route("/count_view")
def count_view():
    global counter
    counter += 1
    return f"This page has been served - {counter} many times!!"


