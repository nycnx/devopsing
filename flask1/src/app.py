from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellohello():
    return "<p>Hello,hello, says Nyco :)</p>"

