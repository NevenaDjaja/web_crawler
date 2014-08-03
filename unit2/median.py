# Find the median of 3 numbers
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
		return bigger(b,c)

# test cases
print(median(1,4,6))
print(median(2,2,2))
print(median(7,8,7))
print(median(2,2,1))