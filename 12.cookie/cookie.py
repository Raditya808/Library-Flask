from flask import Flask, render_template,request,make_response 
# mengimport flask dalam bentuk render template dengan file html / permintaan dan membuat respon

app = Flask(__name__,template_folder='templates')
# inisialisasi aplikasi flask 
# menujukan lokasi file html di templates

@app.route('/',methods=['GET','POST'])
def index():
# routing flask dalam bentuk permintaan dan menampilkan

    if request.method == 'POST':
        # jika metode post di submit

        username = request.form.get('username')
        # akan mengambil data dari username

        resp = make_response(f'''
        <h3>Cokkie saved </h3>
        <p> halo. {username}</p>
        <a href="/"Kembali</a>
        ''')
        # membuat respon html secara langsung 

        resp.set_cookie('username',username)
        return resp
        # menyimpan cookies (username) di browser
        # return respon (resp) yamg sudah termodifikasi

    else:
        username = request.cookies.get('username')
        return render_template('index.html',username=username)
        # ambil cookie (username) dari browser 
        # mengirim variabel (username) ke file render html

if __name__ == '__main__':
    app.run(debug=True)
# untuk menjalankan file flask tersebut 
    
