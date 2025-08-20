🔹 Kode Kedua (Lebih Aman)
import os
from flask import Flask, request 
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'the_file' not in request.files:
            return 'no file apart'
        
        file = request.files['the_file']
        if file.filename == '':
            return 'no file selected'

        filename = secure_filename(file.filename) 
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return f'file upload sukses: {filename}'
        
    return '''
    <form method="POST" enctype="multipart/form-data"><br>
    <input type="file" name="the_file"><br>
    <input type="submit" value="uploads"><br>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

🛠 Fungsi yang digunakan:

secure_filename(file.filename) → membersihkan nama file agar aman dari karakter/path berbahaya.

if 'the_file' not in request.files → validasi apakah field the_file ada di form.

if file.filename == '' → validasi apakah user memilih file atau tidak.

file.save(os.path.join(UPLOAD_FOLDER, filename)) → menyimpan file sesuai nama asli yang sudah diamankan.

📌 Kelebihan: lebih aman, file disimpan sesuai nama asli user.
📌 Kekurangan: sedikit lebih panjang dibanding versi pertama.

⚖️ Perbandingan
Aspek	Kode Pertama	Kode Kedua
Simplicity	✅ Sangat sederhana	❌ Lebih panjang
Keamanan Nama	❌ Tidak aman (selalu overwrite)	✅ Aman (secure_filename)
Cocok untuk	Belajar dasar	Aplikasi nyata
