# ---------------------------------------------------------------------------- #
#                		MRO: Method Resolution Order  	           	      	   #
# ---------------------------------------------------------------------------- #

print('''
-------------------------------------------------------------------------------
			 MRO: Method Resolution Order
-------------------------------------------------------------------------------
	MRO algorithm: http://www.srikanthtechnologies.com/blog/python/mro.aspx
	MRO algorithm: http://www.srikanthtechnologies.com/blog/python/mro.aspx
	Example https://data-flair.training/blogs/python-multiple-inheritance/

	Is a rule that python follows to determine which method to run between 
	the ones existing within inherited class(es)
	"mro()" is an object method listing in which order this would resolve / get 
	the method or attributes needed 
	We can observe it relies on order priority and if not found will search for 
	the closest class defining this value

	🔸 Depth for search
		- can be written like: "M.mro()"
		- can be written like: "M.__mro__"

	🔸 Doing this should be avoided as much as possible
	🔸 This is, in general, not asked for interviews

		---------------------------------------------------
		( python code )
		
		----------------------------------------------------

''')
class A:
	num = 10
	pass

class B(A):
	pass

class C(A):
	num = 1
	pass

class D(B,C):
	pass

print( D.num )


class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.mro())