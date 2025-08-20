# 📂 Flask File Upload — Penjelasan Fungsi

Repository ini berisi **2 versi kode upload file di Flask**.  
Masing-masing kode punya fungsi dan perbedaan tersendiri.  

---

## 🔹 Kode Pertama (Dasar)

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

🛠 Fungsi yang digunakan:

Flask(__name__) → membuat instance aplikasi Flask.

@app.route('/upload', methods=['GET','POST']) → mendefinisikan endpoint /upload yang bisa menerima GET (form) & POST (upload).

request.files → menampung file yang diupload user.

os.makedirs('uploads', exist_ok=True) → membuat folder uploads jika belum ada.

f.save('uploads/uploaded_file.txt') → menyimpan file yang diupload dengan nama tetap uploaded_file.txt.

📌 Kelebihan: sangat sederhana, cocok belajar awal.
📌 Kekurangan: nama file tidak sesuai upload user (selalu overwrite).

