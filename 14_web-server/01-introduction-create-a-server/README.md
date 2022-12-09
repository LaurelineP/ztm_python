## HOW TO RUN THIS FOLDER
### FOLDER 01-introduction-create-a-server
- Set the terminal's location: `01-introduction-create-a-server`
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

