# MarkupSafe escapes characters so text is safe to use in HTML and XML.
# Characters that have special meanings are replaced so that they display as the
# actual characters.

from flask import Flask
from markupsafe import escape


# Flask` is the class we use to instantiate an application.
app = Flask(__name__)


@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return f"user name {username}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show post ID with the given id as integer
    return f"post {post_id}"

