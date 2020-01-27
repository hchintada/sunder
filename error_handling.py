from flask import Flask

app = Flask(__name__)

@app.route('/')
def view():
	return "<h1>Hello World!</>"