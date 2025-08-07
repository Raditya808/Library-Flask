from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Welcome to my web application</h1>
<p>Click <a href="/project">here</a> to go to the project page</p>
<p>Click <a href="/about">here</a> to go to the about page</p>''' 

@app.route('/project')
def project():
    return 'the project page'

@app.route('/about')
def about():
    return 'the about page'


if __name__ == '__main__':
    app.run(debug=True, port=5000)

# kode sederhana membuat dua rute menggunakan syntax html melalui tag a href
