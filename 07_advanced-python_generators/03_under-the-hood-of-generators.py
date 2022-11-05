print('''
		----------------------------------------------------------------------------
		-------------------------- UNDER THE HOOD OF GENERATORS --------------------------
		From prior written code : performance decorators, let's implement a generator instead

	
		''')


def loop_for( iterable ):
	iterator = iter(iterable)
	while True:
		try:
			print(iterator)
			print(next(iterator))
		except StopIteration:
			break

loop_for([ 1,2,3])

# Own range implementation
class Generator:
	current = 0
	def __init__( self, first, last ):
		self.first = first
		self.last = last

	def __iter__( self ):
		return self

	def __next__(self):
		self.current = self.current or self.first
		if self.current < self.last:
			self.current += 1
			return self.current
		raise StopIteration


custom_range = Generator(5,10)
for i in custom_range:
	print(i)


def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break

# Teacher's range implementation
class MyGen:
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last

	# this line allows us to use the current number 
	# as the starting point for the iteration
    MyGen.current = self.first

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration

gen = MyGen(1,100)
for i in gen:
    print(i)

	