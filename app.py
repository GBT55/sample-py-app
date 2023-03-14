from flask import Flask
app = Flask(__name__)

@app.route('/py')
def hello_world():
    return 'Hello, Docker!'