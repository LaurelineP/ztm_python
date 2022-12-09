

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