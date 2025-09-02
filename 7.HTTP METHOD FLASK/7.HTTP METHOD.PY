from flask import Flask, request

app = Flask(__name__)


# membuat variabel baru dalam bentuk def dan return daalm form dalam bentuj menampilkan /POST
def show_login_form():
    return'''
    <h3>Form Login</h3>
        <form method="POST">
            Nama: <input type="text" name="nama"><br>
            Sandi: <input type="password" name="sandi"><br>
            <input type="submit" value="Login">
        </form>
'''
# membuat if statement dan membuat variabel baru 
def do_the_login():
    nama = request.form.get('nama')
    sandi = request.form.get('sandi')
    if nama == 'admin' and sandi == '123':
        return 'Login berhasil'
    else:
        return 'Login gagal'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_login_form()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
