print('''
	Objective: create a fibonacci sequence :
	- using generator function
	- using list
''')
def fib_gen(number):
	try:
		for i in range( number ):
			num = 0
			if( i == 0):
				num = i * i
				fib.append( num )

			else: num = i * 1
			yield 1
	except TypeError as err:
		print( 'Error:', err )


def fib_list(number):
	fibonacci = []
	try:
		for i in range( number ):
			num = 0
			if i == 0: num =  i
			else: num = i * (i+1)
			fibonacci.append( num )
	except TypeError as err:
		print( 'Error:', err )

	return fibonacci


def fib(n):
	a = 0
	b = 1
	for _ in range(n):
		yield a
		local = a
		a = b
		b = local + b

# for x in fib(21):
# 	print( x )

def fib2(n):
	prevFibN = 0
	nextFibN = 1
	result = []
	for _ in range(n):
		result.append(prevFibN)
		local = prevFibN
		prevFibN = nextFibN
		nextFibN = local + nextFibN
		print( 'b', int(prevFibN))
	return result


# print( fib2(20) )

def custom( n ):
	until = n + 1
	result = []
	for _i in range(until):
		i = int(_i)
		if i == 0:
			result.append( i )
		else:
			x = result[i - 1] + i + 1
			result.append( x )
	return result


res = custom(20)
print( res )