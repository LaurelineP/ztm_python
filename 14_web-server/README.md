

# DEV INSTALLATION
- __Install flask__: `python install flask`
- __Install a virtual environment__: `python -m venv venv`
- __Set virtual environment interpreter__: `source venv/bin/activate`
	- _the `activate` file may vary, with an extension, depending on your shell options_
-__Install Flask__: `pip install Flask`
- __Run the server__: `flask run`

## Note:
- OS: mac
- Python: 3.10.6
- pip: 22.2.1

# 13 - WEB DEVELOPMENT WITH PYTHON

Website communicates to a server.
A page is serve from the server that may send the files to display in a browser,
through http/-s protocol




## Building server with Flask
### ⚙️ Setting up Flask
- Frameworks to built server easily
	- [ Flask Documentation ](https://flask.palletsprojects.com/en/2.2.x/) ( recent link / not from course - provided an old one )
		- Is a micro framework: Lean / small library
		- Flask proposes a built tool to set server quickly ( rel: http server from python not being for production )
	- [ Django Documentation ](https://www.djangoproject.com/) ( not from course / extra provided )
		- Large framework with more rules to follow than Flask


- Environment and organization
	- [ venv Documentation ](https://docs.python.org/3/library/venv.html)
	- [ Where Python files should be ](https://stackoverflow.com/questions/1783146/where-in-a-virtualenv-does-the-custom-code-go)
	- [ venv refresher ](https://realpython.com/python-virtual-environments-a-primer/)


#### ⬇️ Flask installation (https://flask.palletsprojects.com/en/2.2.x/installation/)
#### 📁 Use HTML, CSS, JS, IMAGES files
Flask layout: https://flask.palletsprojects.com/en/2.2.x/tutorial/layout/
Flask has a method that renders files " render_template()"
- Handling HTML files: Following the Flask layout, HTML files should be in the "templates" folder
- Handling CSS files: Following the Flask layout, HTML files should be in the "static" folder
- Handling favicon.ico: Following the Flask layout, favicons files should be in the "static" folder  

- Basic Approach:
The classical HTML way of getting static files would be to provide `src`  
the new path leading to `static` folder
All the files' `src` should be equal `/static/<file.extension>`

- Flask Approach:
Flask/Url building: https://flask.palletsprojects.com/en/2.2.x/quickstart/#url-building
Flask provides a built-in templating engine that allows one to inject 
dynamical value into the static file(s) HTML
To do so we need to interpolate ( tell Flash it will compute some Python )  
to display. This is done by wrapping the python code with two   
opening and closing curly braces.  

The engine allows to use built-in functions such as, here,   
`for_url(<FOLDER-PATH>, filename=<FILENAME>)`





```HTML
<!-- BASIC APPROACH ( HTML ) -->
<link rel = "stylesheet" type="text/css" href="static/styles.css" />
<link rel="icon" type="image/png" href="/static/android-chrome-512x512.png" sizes="16x16">
<link rel="icon" type="image/png" href="/static/android-chrome-192x192.png" sizes="16x16">
<link rel="icon" type="image/png" href="/static/apple-touch-icon.png" sizes="16x16">
<link rel="icon" type="image/png" href="/static/favicon-16x16.png" sizes="16x16">
<link rel="icon" type="image/png" href="/static/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/ico" href="/static/favicon.ico" sizes="96x96">

<!-- FLASK STATIC APPROACH -->
<link rel = "stylesheet" type="text/css" href="static/styles.css" />
<link rel="icon" type="image/png" href="{{url_for('static', filename='android-chrome-512x512.png')}}" sizes="16x16">
<link rel="icon" type="image/png" href="{{url_for('static', filename='android-chrome-192x192.png')}}" sizes="16x16">
<link rel="icon" type="image/png" href="{{url_for('static', filename='apple-touch-icon.png')}}" sizes="16x16">
<link rel="icon" type="image/png" href="{{url_for('static', filename='favicon-16x16.png')}}" sizes="16x16">
<link rel="icon" type="image/png" href="{{url_for('static', filename='favicon-32x32.png')}}" sizes="32x32">
<link rel="icon" type="image/ico" href="{{url_for('static', filename='favicon.ico')}}" sizes="96x96">
```

### Use Variable Rules
Those are custom and dynamic value given to the url after an endpoint - a slug
This slug allows to be used in your code afterward and generally condition
what the page displays
https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

Example
```Python
@app.route('/<username>')
def home(username):
	return render_template("index.html", username = "username")
```

## Resources
- Favicon.io - favicon generator : https://favicon.io/favicon-generator/
- MIME: request incorporate the type of data it is transfered between the browser and the server : 
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types


# Portfolio project
- create a server to serve files from a template
- connect the files links with the correct files path  
( according to flask project structure )
- connect requests the front end makes against the server by importing request and checking the data received
https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
- emulate a database to avoid losing sent messages with a text file
- emulate a database to avoid losing sent messages with a csv file
https://docs.python.org/3/library/csv.html




## HOW TO RUN THIS FOLDER
### FOLDER <x-subfolder-of-14-web-server-folder>
- Set the terminal's location: `cd 14_web-server/<x-subfolder-of-14-web-server-folder>`
- Run flask router/server: 
	- if the main script is called `app.py`: `flask run` ( this is the case )
	- if the main script is called `<smth>.py`: 
		- in your terminal set a global variable for Flask to read the correct file:
		`FLASK_APP=<filename>.py`
		- then run `flask run`
- If .txt or .csv files are present and want to witness the creation of them - remove them  
✅ The code supports the file creation when a mail would have been sent through the website
( Those files are mimicking a database storage / here it allows to not loose emails sent )
- Otherwise any email sent would be aggregated to the files ( both .txt and .csv files )


## DEPLOYING A PYTHON SERVER
Python anywhere: https://www.pythonanywhere.com/
Python anywhere is a cloud service that allows one to
host a python server
For the free tier it will auto generate the domain name
( it is customizable if one pays their services )

- Create a free account at python anywhere
- Dashboard > All web apps > Open Web Tab
- Bash
- Create a github repository for the deployment
	- create a new repository - the repository would be cloned from python anywhere bash
	- prepare your local project to be pushed to Github
		- in project terminal - save environment's requirements: `pip freeze > requirements.txt`
		see doc: https://pip.pypa.io/en/stable/cli/pip_freeze/
		- copy all previous code except `venv` and `__pycache__` folders  
		and files `.emulated-database` files
		*A new environment will be built into python anywhere*
		*the program will be able to generate both files when*
		*an email will be sent*
		- push the project to the new repository
- Import project to python anywhere
	- in python anywhere > Dashboard > Consoles > bash
	- clone the repository ( https way )
	- in files tab: all the project files would be loaded and listed in this tab
	- in web tab: add a new web app
		- Create a new web app modal/your web app domain name explanation: click next 
		- Create a new web app modal/select a python framework > manual configuration
		- Create a new web app modal/select a python version ( the one used by the project )
		- Create a new web app modal/manual configuration information WSGI ( the one used by the project ) > next
		- Now a redirection is made to the web tab with a new link toward the new domain created
		```LaurelineP.pythonanywhere.com```
		This is a pre-setted web app that is currently served
- Configure the environment with imported project
	Python anywhere with flask: https://help.pythonanywhere.com/pages/Flask/
	- in Consoles > bash
		- create a virtual env: mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv
		- install flask: pip install flask
		- install any other dependencies if needed : cd <project-folder> && pip install -r requirements.txt ( did not work from requirements )
		- indicate it will work with which environment : workon my-virtualenv
	- in Web tab
		- go to section virtual env and add the name of the virtual environment folder: `my-virtualenv`
		- reload the app ( domain will be serve with flask from that env ) / still not the project updated with the project content
		- go to code section > click on link WGSI configuration file to modify it
			- remove everything but the # Flask commented part
			- uncomment path variable
			- adjust path with the name of your folder
			- uncomment `if` condition
			- uncomment `from __main__ ...`
			- replace `from __main__ ... line` with `from app import app as application`
			- save the file
		- go back to web tab and "reload <app-url>"
		- once reloaded > click on the link and the app would be available

App link : https://LaurelineP.pythonanywhere.com


### Resources: 
How requirements.txt works: https://www.idkrtm.com/what-is-the-python-requirements-txt/