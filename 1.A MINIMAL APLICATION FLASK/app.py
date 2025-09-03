from flask import Flask

app = Flask(__name__)


# contoh kode dalam web
#=====================================
#@app.route("/")                   #==
#def hello_world():                #==
    #return "<p>Hello, World!</p>" #==
#=====================================



# contoh kode untuk menjalankan web app flask
#===========================================
@app.route('/')                     #=======
def hello_world():                  #=======
    return "hello world"            #=======
                                    #=======
@app.route('/hello')                #=======
def helo_world():                   #=======
    return "<h1>hello world</h1>"   #=======
#===========================================


if __name__ == "__main__":
    app.run(debug=True, port=5000)
