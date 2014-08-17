# Finds the median of 3 numbers using two helper methods
# bigger and biggest
def bigger(a,b):
	if a>b:
		return a
	else:
		return b

def biggest(a,b,c):
	return bigger(a,bigger(b,c))

def median(a,b,c):
	big = biggest(a,b,c)
	if big == a:
		return bigger(b,c)
	elif big == b:
		return bigger(a,c)
	else:
		return bigger(a,b)
