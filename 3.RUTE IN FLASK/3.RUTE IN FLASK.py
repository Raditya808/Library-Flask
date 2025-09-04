from flask import Flask

app = Flask(__name__)


# kode flask dengan dua route

# contoh kode nya di web
#=====================================================
# langsung masuk di tampilan web utama      #=========
#@app.route('/')                            #=========
#def index():                               #=========
    #return 'index page'                    #=========
                                            #=========
                                            #=========
                                            #=========
#@app.route('/hello')                       #=========
#def hello():                               #=========
    #return 'Hello, World'                  #=========
# jika dijalankan http:127.0.0.1.5000/      #=========
# hello maka akan mengeluarkan              #=========
# Hello world                               #=========
#=====================================================


@app.route('/')
def tanpa_slash():
    return '<h1>Selamat Datang Di Tampilan Web Utama Ketik /Radit Untuk Ke Rute Kedua Ketik /halo Ke Rute Tiga</h1>'

# masuk di 127.0.0.1.5000/Radit 
# maka akan menampilkan hello radit dalam return 
@app.route('/Radit')
def radit():
    return'hallo radit'


@app.route('/halo')
def halo():
    return 'Halo bro'
# http juga harus diikut dengan huruf yang sama jika tidak maka route tidak dikenali 


# syntax untuk menjalankan file lewat a minimal application 
if __name__ == '__main__':
    app.run(port=5000)

