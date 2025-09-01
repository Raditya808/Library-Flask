import os

from flask import Flask, request 
# flask dalam bentuk app dan dibuat ke request

from werkzeug.utils import secure_filename
# membersihkan nama file agar aman    

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

os.makedirs('uploads', exist_ok=True)

@app.route('/upload', methods=['GET', 'POST']) # rute ini upload ini mrmbuat dalam bentuk get dan post untuk proses upload
def upload_file():
    if request.method == 'POST':
        if 'the_file' not in request.files:
            return 'no file apart'
        print(request.files) # output file yang akan di upload di terminal     
        # proses jika tidak ada <input type="file" name="the_file">
        # dalam html jinja dibawah maka akan eror
        

        file = request.files['the_file']
        # mengambil objek file
        if file.filename =='':
            return 'no file selected'
        # if statement cek apakah user memilih file(nama kosong berarti tidak ada file)

        filename = secure_filename(file.filename) # membuang karakter berbahaya/ path berbahaya
        file.save(os.path.join(UPLOAD_FOLDER,filename))
        return f'''file upload sukses: {filename}
     <br><input type="button" value="/upload"> 
        '''
        
    

    return '''

    <form method="POST" enctype="multipart/form-data"><br>
    <input type="file" name="the_file"><br>
    <input type="submit" value="uploads"><br>
    </form>
    '''

if (__name__) =='__main__':
    app.run(debug=True)
