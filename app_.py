"""
# how to run your application in debug mode?

flask --app <file-name> --debug run

"""

import json
from flask import Flask, request


app = Flask(__name__)


class MyDB:
    foo = []


@app.get("/data")
def get_data():
    return f"<h1> data available - {MyDB.foo}</h1>"


@app.post("/data")
def post_data():
    body = request.data  # byte-string
    data_ = json.loads(body)  # serializing byte-string into `dict`
    for value_ in data_.values():
        MyDB.foo.append(value_)
    return f"<h1> latest data {MyDB.foo} </h1>"


if __name__ == "__main__":
    print("hello world")
    app.run(debug=True)





