dalam flask pasti ada yang namanya route atau rute dalam website

fungsi rute adalah lokasi website tergantung kita mengetik didalam website nya tersendiri melalui kode http://127.0.0.1:5000/

garis miring setelah port 5000 adalah lokasi dimana kita menuju rute web yang kita tuju

dalam kode tersebut kita membuat dua rute dalam satuu syntax flask

ketika rute didalam syntax seperti ini 


@app.route('/') ---> ini tidak ada nama di setelah garis miring yang artinya jika masuk http://127.0.0.1:5000 langsung ke rute index tanpa memasukan nama rute 
def index():
    return 'index page' ---> output web tersebut


@app.route('/hello') ---> ini memiliki nama setelah garis miring saat di akses http://127.0.0.1:5000/hello maka tampilan web / rute web berubah ke hello
def hello():
    return 'Hello, World' ---> output web tersebut

