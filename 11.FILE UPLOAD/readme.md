# 📂 Flask File Upload — Dua Versi Implementasi

Repository ini berisi **dua contoh implementasi upload file dengan Flask**.  
Tujuannya untuk memahami dasar cara kerja `request.files` hingga versi yang lebih aman menggunakan `secure_filename`.

---

## 🔹 Kode Pertama (Versi Dasar)

```python
from flask import Flask, request 
import os

app = Flask(__name__)           

@app.route('/upload', methods=['GET', 'POST'])     
def upload_file():
    if request.method == 'POST':
        print(request.files)
        print(request.files['the_file'].filename)
        os.makedirs('uploads', exist_ok=True)  

        f = request.files['the_file']
        f.save('uploads/uploaded_file.txt')

        return 'file uploaded successfully'

    return '''
    <form method="POST" enctype="multipart/form-data"><br>
    <input type="file" name="the_file"><br>
    <input type="submit" value="upload"><br>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

===========================================================================================================

🔹 Kode Kedua (Versi Lebih Aman)
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
===========================================================================================================
🛠 Fungsi Utama

secure_filename(file.filename) → mengamankan nama file dari karakter berbahaya.

if 'the_file' not in request.files → validasi apakah form mengandung input file.

if file.filename == '' → validasi apakah user memilih file.

file.save(os.path.join(UPLOAD_FOLDER, filename)) → menyimpan file dengan nama asli (yang sudah diamankan).
===========================================================================================================


``` bash
pip install flask
```

``` bash
python upload_basic.py     # kode pertama
python upload_secure.py    # kode kedua
```

``` bash
http://127.0.0.1:5000/upload
```


