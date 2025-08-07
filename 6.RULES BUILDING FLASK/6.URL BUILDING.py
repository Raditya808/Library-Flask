from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index' '<br>' '<a href="/login">Login</a>'

@app.route('/login')
def login():
    return 'ini page login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
app.run(debug=True, port=5000)
    