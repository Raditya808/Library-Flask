Kode berikut menggunakan app.test_request_context() dari Flask untuk membuat konteks permintaan (request context) palsu, agar fungsi url_for() dapat dipanggil di luar request sebenarnya (misalnya, dalam shell Python atau saat pengujian). Mari kita bahas satu per satu:

python
Copy
Edit
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
Penjelasan:
1. url_for('index')
Membangkitkan URL untuk endpoint (fungsi route) bernama index.

Contoh output:

Copy
Edit
/
(Tergantung pada bagaimana route index didefinisikan: @app.route('/').)

2. url_for('login')
Membangkitkan URL untuk endpoint bernama login.

Contoh output:
/login

3. url_for('login', next='/')
Membangkitkan URL untuk login dengan parameter query string.

Contoh output:
/login?next=/

4. url_for('profile', username='John Doe')
Membangkitkan URL untuk endpoint profile yang memerlukan argumen username. Jika route-nya seperti ini:

@app.route('/user/<username>')
def profile(username):
    ...
Maka url_for() akan meng-encode karakter dalam username.

Contoh output:
/user/John%20Doe

contoh ouput diatas adalah ketika salah satu url di copy di web maka akan terpanggilkan 

Catatan:
Fungsi url_for(endpoint, **values) digunakan untuk menghasilkan URL absolut atau relatif berdasarkan nama fungsi view (endpoint).

Nilai parameter seperti 'John Doe' akan di-URL encode menjadi %20 untuk spasi.