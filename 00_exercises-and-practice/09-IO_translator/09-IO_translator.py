from deep_translator import GoogleTranslator
print('''
-----------------------------------------------------------------------------------
				I/O - INPUT OUTPUT - TRANSLATOR
-----------------------------------------------------------------------------------
	🔸 Objective:
		Translate the content from a file using what has been seen
		( modules, packages, handling files )
-----------------------------------------------------------------------------------
''')


def translate(path):
	# gets file path from path to create the new file
	same_path = path.split('/')
	same_path.pop()
	same_path = '/'.join(same_path) + '/'
	translation_file_path = f'{same_path}_translated.txt'
	print( same_path )
	try:
		# gets text from original file
		text = ''
		with open(path) as _file:
			text = _file.read()
		translated = GoogleTranslator('fr', 'ja').translate(text)

		# write a new file with translation
		with open(translation_file_path, "w") as translation_file:
			translation_file.write(translated)

		# print new file content
		with open(translation_file_path) as translated_file:
			print(f'[ FROM CREATED FILE - reading ]: { translated_file.read()}')

	except (FileNotFoundError, IOError) as error:
		print('an error occurred: ', error )


file = '../assets/09-IO_original.txt'
translate(file)
