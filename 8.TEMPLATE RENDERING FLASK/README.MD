🧪 Penjelasan Per Bagian
✅ markup1 = '<blink>HACKER</blink>'
Ini HTML mentah (raw).

Di template, akan di-escape otomatis, jadi tag <blink> tidak bekerja di browser.

✅ markup2 = Markup('<strong>Hello %s!</strong>') % markup1
markup1 dimasukkan ke dalam string HTML menggunakan Markup.

Karena markup1 bukan Markup, maka isinya di-escape otomatis.

Hasil: tag <blink> tidak aktif (ditampilkan sebagai teks literal).

✅ markup3 = Markup('<em>Marked up</em> &raquo; HTML')
Ini adalah string HTML aman (sudah ditandai pakai Markup).

Akan dirender apa adanya, jadi tag <em> dan simbol &raquo; muncul.

✅ markup3.striptags()
Menghapus semua tag HTML, hanya teks biasa yang ditampilkan.

Contoh hasil: "Marked up » HTML"

🖼️ Output di Browser
markup1: Tampil sebagai teks literal, <blink> tidak aktif.

markup2: Tampil dengan "Hello" tebal, tapi isi dari markup1 tetap di-escape.

markup3: Tampil dengan teks miring dan ».

markup3.striptags(): Tampil sebagai teks polos.

🔐 Kesimpulan
Kode ini menunjukkan:

Otomatisasi escape HTML di Flask untuk mencegah XSS.

Peran Markup untuk menandai string sebagai HTML yang aman.

Cara menghapus tag HTML via .striptags().