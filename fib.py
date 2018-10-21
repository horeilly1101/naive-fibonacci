'''
contains a naive recursive implementation of 
the fibonacci sequence
'''

def fib(num):
	'''
	returns the ith element of the fibonacci
	sequence

	kw args:
		num -- an integer greater than or
			equal to zero
	'''
	return 1 if (num == 1 or num == 0) \
		else fib(num-1) + fib(num-2)