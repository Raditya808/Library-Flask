# 📂 Flask File Upload — Dua Versi Implementasi

Repository ini berisi **dua contoh implementasi upload file dengan Flask**.  
Tujuannya untuk memahami dasar cara kerja `request.files` hingga versi yang lebih aman menggunakan `secure_filename`.

``` bash
pip install flask
```
``` bash
127.0.0.0.1
```
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
