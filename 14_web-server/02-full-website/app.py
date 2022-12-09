from flask import Flask, render_template, request, redirect
import json
from datetime import datetime as Date

import uuid
app = Flask(__name__)
fileNames = {
	"js" : "main.70a66962.js",
	"css":"main.3f6952e4.css",
}

@app.route('/', methods = ["GET"])
def root_index():
	return render_template('index.html', fileNames = fileNames )



# Classic routing - but we can observe repetitions --> repeated task could be done with loops
def set_classic_rooting():
	@app.route('/index', methods = ["GET"])
	@app.route('/index.html', methods = ["GET"])
	@app.route('/', methods = ["GET"])
	def root_home():
		return render_template('index.html', fileNames = fileNames )



	@app.route('/about')
	@app.route('/about.html')
	def root_about():
		return render_template('about.html')


	@app.route('/works')
	@app.route('/works.html')
	def root_woks():
		return render_template('works.html')


	@app.route('/contact')
	@app.route('/contact.html')
	def root_contact():
		return render_template('contact.html')



# Personal implementation: Uses for loop and os.walk to get files to get to 
def set_dynamic_routing():
	for _,_,f in os.walk('./templates/'):
		@app.route(f'/<f>', methods = ["GET"])
		def root(f):
			return render_template(f, fileNames = fileNames )


# Courses solution : routing with any file mention in url
def set_dynamic_routing_any():
	@app.route('/<string:file_name_in_url>')
	def root(file_name_in_url):
		return render_template(file_name_in_url, fileNames = fileNames)

def store_data_in_file(data):
	print(data)

	with open('./.emulated-database.txt', 'a+') as file:
		email_content = f'''
		date: {Date.now()}
		uuid: {uuid.uuid4()}
		email: {data["email"]}
		subject: {data["subject"]}
		message :
			{data["message"]}

		'''
		file.writelines(email_content)

@app.route('/submit_form', methods = ['POST'])
@app.route('/submit_form.html', methods = ['POST'])
def submit_form():
	if( request.form ):
		request_data = request.form.to_dict()
		print('request data', request_data)
		store_data_in_file(request_data)
		return redirect('thankyou.html')
	else:
		return 'something went wrong'

# set_classic_rooting()
# set_dynamic_routing()
set_dynamic_routing_any()
