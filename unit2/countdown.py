# counts down from input to "Blastoff"
# including doctests in the code
def countdown1(n):
	"""
	>>> countdown1(3)
	3
	2
	1
	Blastoff!
	"""
	while n>0:
		print(n)
		n -= 1
	print("Blastoff!")


def countdown2(n):
	"""
	>>> countdown2(4)
	4
	3
	2
	1
	Blastoff!
	"""
	while True:
		print(n)
		if n==1:
			print("Blastoff!")
			break
		n -= 1
