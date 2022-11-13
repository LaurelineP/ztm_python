print('''
-----------------------------------------------------------------------------------
				I/O - INPUT OUTPUT
-----------------------------------------------------------------------------------
	🔸 FILE - READ WRITE APPEND
	"open()" command has a second optional argument which allows to specify
	for what purpose open would be used - either to
	- read			: open( <file>, mode = 'r' ) - default value when no 2nd arg.
	- read and write	: open( <file>, mode = 'r+' )
	- write			: open( <file>, mode = 'w' )
	- append		: open( <file>, mode = 'a' )
-----------------------------------------------------------------------------------
''')
# READING A FILE
with open('test_file.txt', mode='r') as file:
	print(f'''
	[ READ ] Reading the file:
	{file.read()}
	''')

# READING A FILE AND EDITING IT
with open('test_file.txt', mode='r+') as file:
	print(f'''
	[ READ AND WRITE ] Reading the file and write by overriding the file at
	its beginning
	Writing into the file: {file.write(' 🔹 [ r+ ] editing a file ')}
	Checking where cursor is: {file.tell()}
	''')

# WRITE A FILE
with open('new_file.txt', mode='w') as file:
	print(f'''
	[ WRITE ] Will write into a provided file
		- if the file does exist: executing the command will override all content
		- if the file does not exist: executing the command will create and write
		to the file destination
		
	Writing into the file...: {file.write(' 🔹 [ w ] Creating a file and writing into it ')}
	Checking where cursor is: {file.tell()}
	''')

# APPEND TO A FILE
with open('new_file.txt', mode='a') as file:
	print(f'''
	[ WRITE ] Will write into a provided file
		- if the file does exist: executing the command will override all content
		- if the file does not exist: executing the command will create and write
		to the file destination

	Writing into the file...: {file.write(' 🔹 [ a ] Adding at the end of the file line')}
	Checking where cursor is: {file.tell()}
	''')