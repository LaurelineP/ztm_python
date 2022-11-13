import sys
import pdb

print('''
-----------------------------------------------------------------------------------
				I/O - INPUT OUTPUT
-----------------------------------------------------------------------------------
	🔸 WORKING WITH FILES IN PYTHON
	Allows to manipulate files ( compression, pdf )
		🔹 With built-in function open: opens file
			- <file object>.read() : ️open will read once the file

			- <file object>.seek(<cursor-position>): if instruct after each
				<file object>.read() would allow to read the file multiple time
				( once the value red, the value would not be printable again unless
				using this seek method )

			- <file object>.readline(): will read the number of times the execution is made,
				corresponding each time to first line ( can be executed multiple times )
				Due to the cursor placed ( a bit like yield or calling next())
				
			- <file object>.readlines(): will read all the lines, all the lines are stored
				within a list
				
			- <file object>.close():
			📌Must manually close the file each time
-----------------------------------------------------------------------------------
''')

print('''-----------------------------------------------------------------------------------
	🔸 READING A FILE : CLASSIC WAY
		🔹open a file: store the "open(<file>, [<mode: string])" in a variable
			default second argument is mode = 'r'
		🔹read the file:
			- <file>.read(): read the entire file store the "open(<file>)" in a variable
			This would be red once ( a cursor will read all character one by one -> 
			this represent the cursor through the document. Once red with the read method
			the cursor does not automatically go back to the first character
			So executing multiple time a file using this method would be red once.

-----------------------------------------------------------------------------------
''')

file = open('test_file.txt')

print(f'''
		🔸READ METHOD: reads the entire file
			Syntax: "file.read()"
			File content: {file.read()}
			Try to read once it has been red would not print anything
				- second reading: {file.read()}
				- third reading: {file.read()}
				( nothing in second and third reading )
''')

print(f'''
		🔸TELL METHOD: indicates where the reading cursor is
			Syntax: "file.tell()"
			Checks current cursor state after the use of ".read()" method
				- Cursor position ( character position ): {file.tell()}
''')

# reset reading experience
file.seek(0)
print(f'''
		🔸SEEK METHOD: repositions the cursor / used with read
			would help reading the file multiple times using "file.read()"
			Syntax: file.read() file.seek(0)  
			Checks current cursor state after the use of .read() method
				- 1st Reading: {file.read()}
				
				- reset cursor to zero...: {file.seek(0)}
				
				- 2nd Reading: {file.read()}
''')

print(f'''
		🔸CLOSE METHOD: one must close the file once finished 
			( to avoid using memory unnecessarily )

				- returns "None": {file.close()}

''')

print(file.close())

print('''-----------------------------------------------------------------------------------
	🔸 READING A FILE : MODERN WAY - without having to close the file
		🔹open a file: "with open(<file>) as file:" statements
			then indent to write the instructions to use the file
		🔹read the file:
			- <file>.read(): read the entire file store the "open(<file>)" in a variable
			This would be red once ( a cursor will read all character one by one -> 
			this represent the cursor through the document. Once red with the read method
			the cursor does not automatically go back to the first character
			So executing multiple time a file using this method would be red once.

-----------------------------------------------------------------------------------
''')


with open('test_file.txt', mode='r+') as file:
	print('\n -->', file.read())

	file.seek(0)
	print('\n\n-->', file.readline())

	file.seek(0)
	print('\n\n ---> RESET')
	print('\n\n --->', file.readlines())
	print('\n\n ---> adding new line')
	file.write('🙌 adding new line')
	print('\n\n --->', file.readline())



