# Finds the median of 3 numbers using built-in sort method
def median2(a,b,c):
	result = [a,b,c]
	result.sort()		
	return result[1]
