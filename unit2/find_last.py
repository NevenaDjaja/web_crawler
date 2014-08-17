# Finds the last position of the last occurence of substring s in str
# Input:
# str - string
# s - string, to be searched in str
#
# Output:
# last_pos - number, last position of searched string
def find_last(str,s):
	last_pos = -1
	while True:
		pos = str.find(s,last_pos+1)
		if pos == -1:
			# return the previous position
			return last_pos
		last_pos = pos
