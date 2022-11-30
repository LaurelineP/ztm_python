import os
import smtplib
import sys
from datetime import datetime as date
from dotenv import load_dotenv
from email.message import EmailMessage
from string import Template
# see why pathlib istead of os
# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
from pathlib import Path


# set parent path
sys.path.append('../../__utils')
from __utils.index import print_non_dunder
load_dotenv()
print('''
-----------------------------------------------------------------------------------
				SCRIPT PDF PROCESSING
-----------------------------------------------------------------------------------
	🔸 smtplib: SMTP server is required to send email.
		SMTP Simple Mail Transfer Protocol ( commonly known protocol HTTP-S ) 
	🔸 EmailMessage: lib to construct an SMTP email
	


-----------------------------------------------------------------------------------
''')


# port 465 - takes more time to be executed than SMTP
def send_message_ssl():
	pwd = os.getenv('GMAIL_GEN_PWD')
	message = f'''
	Subject: Using SSL
	Hello, this is one test email,
	Happy day to you!
	( Using SSL )
	{date.now()}
	'''

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
		email_address = 'beta.handler@gmail.com'
		connection.login(email_address, pwd)

		# first param: email address from
		# second param: email address to
		# third param: message content ( no
		connection.sendmail(email_address, email_address, message)


# port 587
def send_message_smtp():
	pwd = os.getenv('GMAIL_GEN_PWD')
	email = EmailMessage()

	# Handling email header: from, to, subject
	email['from'] = 'Beta Handler'
	email['to'] = 'beta.handler@gmail.com'
	email['subject'] = 'SMTP'

	# Handles content
	email.set_content(f'''
		Hello, this is one test email,
			Happy day to you
			( using SMTP )
			{date.now()}
	''')

	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
		# protocol of smtp checking this is a smtp server
		# smtp.ehlo() # works also when commented

		# connects using encryption TLS
		smtp.starttls()

		# login with correct credentials:
		smtp.login('beta.handler@gmail.com', pwd)

		# send message as TLS
		smtp.send_message(email, pwd)


def send_message_html():
	pwd = os.getenv('GMAIL_GEN_PWD')
	email_address = 'beta.handler@gmail.com'

	html = Path('email.html').read_text() # read as string
	html = Template(html) # read as template to pass dynamic value

	dynamic_values = {
		'name': 'Beta'
	}
	html = html.substitute(dynamic_values)

	email = EmailMessage()
	email['from'] = email_address
	email['to'] = email_address
	email['subject'] = 'SMTP x HTML'
	email.set_content(html, 'html')

	with smtplib.SMTP('smtp.gmail.com', 587 ) as smtp:
		smtp.starttls()
		smtp.login(email_address, pwd)
		smtp.send_message(email)


send_message_ssl()
send_message_smtp()
send_message_html()


print('all done')
