kode memiliki 3 rute 
Flask secara otomatis mengonversi bagian URL berdasarkan tipe data yang kamu tentukan di konverter URL-nya.


-@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {escape(username)}"

rute ini akan menjalankan kode dengan http://127.0.0.1:5001/user/radit
maka saat dijalankan di website maka output nya akan mengeluarkan nama 

dan route selanjut nya

-@app.route('/post/<int:post_id>')
def post_id(post_id):
    return f"Post ID: {post_id}"

rute ini akan menjalankan kode dengan http://127.0.0.1:5001/
bedanya kode ini ada hubungan nya dengan sebuah tipe data int / integer 
dimana pengguna menjalankan di web dengan kode http://127.0.0.1:5001/post/19


dan route terakhir

-@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath: {escape(subpath)}"

rute ini akan menjalankan kode dengan http://127.0.0.1:5001/path/""/ atau tanpa titik 
dimana pengguna menjalankan web dengan kode http://127.0.0.1:5001/path/""/tanpa titik
maka output nya subpath: "test" atau tes


✅ Fungsi Kode Flask 
1. @app.route('/user/<username>')
username adalah variabel string dari URL.

Contoh URL: http://localhost:5001/user/radit

Hasil: User radit

Gunakan escape() agar aman dari XSS.

📌 Tipe data: str (string)

2. @app.route('/post/<int:post_id>')
post_id hanya bisa menerima angka bulat (integer).

Contoh URL: http://localhost:5001/post/123

Hasil: Post ID: 123

Jika kamu akses /post/abc ➜ ❌ Error 404 (karena bukan angka)

📌 Tipe data: int

3. @app.route('/path/<path:subpath>')
subpath bisa berisi teks dengan garis miring /, misalnya folder atau path file.

Contoh URL: http://localhost:5001/path/folder/berkas.txt

Hasil: Subpath: folder/berkas.txt

Aman dari XSS karena pakai escape()

📌 Tipe data: str, tapi boleh mengandung /

🔎 Apa Hubungannya dengan Tipe Data?
Ya, Flask pakai konverter seperti:

Konverter	Tipe Data Python	Contoh URL
(default)	str	/user/<username>
int	int	/post/<int:post_id>
float	float	/value/<float:x>
path	str (dengan /)	/path/<path:subpath>


jenis konverter

string         (default) menerima teks apa pun tanpa garis miring

int             menerima bilangan bulat positif

float           menerima nilai floating point positif

path            suka stringtetapi juga menerima garis miring

uuid            menerima string UUID