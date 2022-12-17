import os


def save_test(url, content):
	filename = ".test-logs.txt"

	is_created = os.path.exist(filename)

	try:
		with open(filename, 'w+') as test_file:
			# Init file
			if not is_created:
				print('adding not created')

				test_file.write('''
					================== TEST LOGS ================
					
					Testing: {url}
					
					=============================================
					
				''')
			else:
				print('adding')
				test_file.write(content)
	except: print('[ WRITE FILE ] - no file was created ')