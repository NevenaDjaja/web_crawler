def median2(a,b,c):
	result = [a,b,c]
	result.sort()		
	return result[1]

# test median2
print(median2(5,4,6))
print(median2(7,3,2))
print(median2(3,4,3))