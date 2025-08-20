# 📂 Flask File Upload (Versi Aman)

Contoh implementasi **upload file di Flask** dengan validasi dan penanganan nama file yang lebih aman menggunakan `secure_filename` dari **Werkzeug**.

---

## 🚀 Kode Lengkap

```python
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
