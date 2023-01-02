"""
How to run flask application?

```
flask --app main run

flask --app main run --port 8080

# How to publish your application to public IP?

flask --app main run --port 8080 --host 0.0.0.0
```

Use control + c to stop server

"""

from flask import Flask

# Flask is the most important class to create an `application`
app1 = Flask(__name__)


# We use `app.route()` decorator to tell flask about relative URL
@app1.route("/")
def hello_world():
    return "<p> hello world!! </p>"


@app1.route("/details")
def get_details():
    return "<p> Prashant - Python - Velocity </p>"
