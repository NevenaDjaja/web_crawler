# find the last position of the last occurence of substring s in str
def find_last(str,s):
	last_pos = -1
	while True:
		pos = str.find(s,last_pos+1)
		if pos == -1:
			# return the previous position
			return last_pos
		last_pos = pos

# test find_last
print(find_last("find me if you find me yet","me"))
print(find_last("111111111", "1")) 
print(find_last('aaaaa', 'aa'))