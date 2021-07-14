from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome, my name is Moustafa Elsayed and this is my app"


app.run(host="0.0.0.0", port=8080)
