from flask import Flask, request


app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(host='    
    
    
    # kode ditas hanya berjalan di terminal saja tapi 
    # dikarenakan tidak ada route yang 
    # ditentukan maka hanya menampilkan eror 404