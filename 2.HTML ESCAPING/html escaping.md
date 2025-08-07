kode ini sama berjalan di port angka yang sama meskipun kalau port diganti dengan angka lain didepan selagi port yang dijalankan dibelakang adalah 5000 maka kode tetep akan berjalan di terminal sebagaimana mestinya

kode flask sederhana ini jika kita mengakses nya di http://127.0.0.1:5000/(nama kita)

maka output yang keluar di web adalah Hello, (name)!

📌 Penjelasan Kode untuk Pemula
1. from flask import Flask
👉 Ini mengimpor Flask, yaitu alat (library) untuk membuat aplikasi web dengan Python.

2. from markupsafe import escape
👉 Ini mengimpor fungsi escape(), fungsinya:

Melindungi website kamu dari kode berbahaya

Misalnya: orang iseng masukkan kode <script> supaya bisa muncul alert/popup di browser

escape() akan mengubah <script> jadi teks biasa, bukan dijalankan

3. app = Flask(__name__)
👉 Ini membuat aplikasi Flask. Kamu bisa bayangkan ini seperti membuat mesin yang siap menerima permintaan dari pengguna lewat browser.

4. @app.route("/<name>")
👉 Ini bagian penting:

Flask akan menjalankan fungsi hello() jika URL-nya ada nama di belakang garis miring /.

Contoh URL: http://127.0.0.1:5000/John
Maka name = "John"

5. def hello(name):
👉 Fungsi ini menerima input nama dari URL, lalu menjalankan perintah di dalamnya.

6. return f"Hello, {escape(name)}!"
👉 Ini yang dikembalikan ke pengguna (ditampilkan di browser):

Contoh kalau nama: John, maka tampil: Hello, John!

Tapi kalau nama: <script>alert("x")</script>, maka tampil:
Hello, &lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;!
➤ Ini tidak akan dijalankan, karena sudah di-escape

📌 Inilah yang dimaksud di web resmi Flask:

Setiap nilai yang diberikan pengguna yang ditampilkan dalam output harus di-escape untuk melindungi dari serangan injeksi (XSS).
escape() bisa digunakan secara manual untuk itu.

XSS adalah singkatan dari Cross-Site Scripting, yaitu serangan keamanan pada aplikasi web yang memungkinkan penyerang menyisipkan kode JavaScript berbahaya ke dalam halaman web yang dilihat oleh pengguna lain.

➡️ Tujuannya bisa untuk:

Mencuri data pengguna (seperti cookie, sesi login)

Menampilkan pop-up palsu

Merusak tampilan halaman

Mengarahkan pengguna ke situs palsu



7. if __name__ == "__main__":
👉 Ini perintah standar Python: artinya jalankan aplikasi Flask-nya kalau file ini dijalankan langsung.


