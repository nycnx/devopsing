from flask import Flask

app = Flask(__name__)

@app.route("/")
def hellohello():
    return "<h>Helloooo says Flask-App number 2</h>"

