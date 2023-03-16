from flask import Flask
app = Flask(__name__)

@app.route('/py')
def hello():
	return "Hello World, this is my first zero-touch pipeline app.py"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
