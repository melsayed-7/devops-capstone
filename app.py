from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome, my name is Mislav and this is my Flask Web App! v1'

app.run(host='0.0.0.0', port=5000)
