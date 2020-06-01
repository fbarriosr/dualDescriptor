def printElement(element, large):
	print element.replace(element, element * large,1)
	return 0
		
def printElementName(name,element, large):
	s = element.replace(element, element * large,1)
	name = ' '+name+' '
	t1 = len(name)
	t2 = len(s)

	position = t2/2 - t1/2 -1

	s = s[:position] + name + s[position+t1:]
	print s

	return 0

	
