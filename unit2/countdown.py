# count down from input to "Blastoff"
def countdown1(n):
	while n>0:
		print(n)
		n -= 1
	print("Blastoff")


def countdown2(n):
	while True:
		print(n)
		if n==1:
			print("Blastoff!")
			break
		n -= 1


# test cases
countdown1(3)
countdown1(10)
countdown2(3)
countdown2(1)