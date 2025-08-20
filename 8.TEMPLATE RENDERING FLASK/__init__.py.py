from flask import Flask, render_template
from markupsafe import Markup

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    markup1 = '<blink>HACKER</blink>'
    markup2 = Markup('<strong>Hello %s!</strong>') % markup1  # HTML akan di-escape
    markup3 = Markup('<em>Marked up</em> &raquo; HTML')
    return render_template("hello.html", markup1=markup1, markup2=markup2, markup3=markup3)

@app.route('/hello1')
@app.route('/hello1/<name>')
def hallo1(name=None):
    return render_template('hello2.html',person=name)

if __name__ == "__main__":
    app.run(debug=True)

