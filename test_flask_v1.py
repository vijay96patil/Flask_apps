"""
How to run flask application?

```f
flask --app main run
```

"""

from flask import Flask

app1 = Flask(__name__)


@app1.route("/")
def hello_world():
    return "<p> hello world!! </p>"




