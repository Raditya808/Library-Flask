from flask import Flask , request, render_template 

app = Flask(__name__)


def valid_login(username, password):
    return username == 'admin' and password == 'secret'


def log_the_user_in(username):
    return f'Logged in as {username}'

@app.route('/',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

 # kode ini membuat suatu web aplikasi sederhana dengan Flask 
 # yang menangani login.
 # dengan key yang bernama username dan password
 # dengan nama admin dan password sebagai secret
 
 # jika salah memasuukan nick dan password 
 # maka akan terjadi error di kode html

