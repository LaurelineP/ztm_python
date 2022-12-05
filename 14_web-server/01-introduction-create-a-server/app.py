from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root_home():
	try:
		return render_template('index.html')
	except Exception as error:
		return '40004'

@app.route('/<username>')
def root_home_user(username):
	try:
		return render_template('index.html', username = username)
	except Exception as error:
		return '40004'