import os   
# syntax import untuk membuat file upload kalau belum ada

from flask import Flask,request 
# mengimport flask menjadi objek permintaan atau request

app = Flask(__name__)           
# mengubah Flask dalam bentuk app

@app.route('/upload',methods=['GET','POST'])     
# definisi rute /upload

# bisa diakses via GET (untuk form html) dan POST (proses upload)

def upload_file():
    if request.method == 'POST':
        print(request.files)
        print(request.files['the_file'].filename)
        os.makedirs('uploads', exist_ok=True)  
        # Ensure the uploads directory exists

        f = request.files['the_file']
        f.save('uploads/uploaded_file.txt')

        # akan ter save dalam bentuk file.txt 
        # folder txt yang dimana ada kode kode aneh didalam
        return 'file uploaded successfully'
# jika pengguna submit from (POST) Flask akan menaruh file di request.file
# debug print akan mmebantu lihat file yang akan di upload ke browser

    return '''
    <form method="POST" enctype="multipart/form-data"><br>
    <input type="file" name="the_file"><br>
    <input type="submit" value="upload"><br>
    </form>
    '''
# dan ini adalah form html yang akan digunakan untuk upload file

# kode sederhana untuk mengupload file di flask

if (__name__)=='__main__':
    app.run(debug=True)


