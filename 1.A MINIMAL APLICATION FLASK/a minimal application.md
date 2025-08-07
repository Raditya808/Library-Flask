Jadi apa yang dilakukan kode itu?

Pertama, kita mengimpor Flaskkelasnya. Contoh kelas ini akan menjadi aplikasi WSGI kita.

Selanjutnya, kita buat instans kelas ini. Argumen pertama adalah nama modul atau paket aplikasi. __name__Ini adalah pintasan praktis yang sesuai untuk sebagian besar kasus. Ini diperlukan agar Flask tahu di mana harus mencari sumber daya seperti templat dan berkas statis.

Kami kemudian menggunakan route()dekorator untuk memberi tahu Flask URL mana yang harus memicu fungsi kami.

Fungsi ini mengembalikan pesan yang ingin ditampilkan di peramban pengguna. Tipe konten default adalah HTML, sehingga HTML dalam string akan dirender oleh peramban.

Simpan sebagai hello.pyatau yang serupa. Pastikan untuk tidak memanggil aplikasi Anda flask.pykarena ini akan menimbulkan konflik dengan Flask itu sendiri.

Untuk menjalankan aplikasi, gunakan flaskperintah atau . Anda perlu memberi tahu Flask di mana aplikasi Anda berada dengan opsi tersebut.python -m flask--app

maka kode ini akan berjalan di port seperti dibawah

$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * output yamg keluar dari kode tersebut adalah halo dunia

 source : https://flask.palletsprojects.com/en/stable/