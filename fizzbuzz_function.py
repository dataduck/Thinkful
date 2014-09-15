import sys 

def divide(a,b):
	"""Is one number evenly divisable by another"""
	return a % b == 0



def fizzbuzz(limit):
	"""Prints number/fizz/buzz/fizz buzz when iterating to the upper limit"""

	for i in range(1, limit+1): 
		if divide(i, 15):
			print "fizz buzz"
		elif divide(i, 5): 
			print "buzz"
		elif divide(i, 3): 
			print "fizz"
		else: 
			print i

#if __name__ == '__main__':
#	limit = int(sys.argv[1])
#	fizzbuzz(limit)

print fizzbuzz(15)