
def shorter_links(mystring):
	newstring = []
	lastString = []
	result = ""   
	cnt = 0

	for each in mystring:	
		if cnt >= 8:
			newstring.append(each)
		cnt = cnt + 1

	for x in newstring:
		lastString.append(x)
		if x == '/':
			break
		
	for j in lastString:
		result = result + j 
	return result

