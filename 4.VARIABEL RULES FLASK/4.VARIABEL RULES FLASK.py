from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def post_id(post_id):
    return f"Post ID: {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath: {escape(subpath)}"

if __name__ == "__main__":
    app.run(debug=True, port=5001)