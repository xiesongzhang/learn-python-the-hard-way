def sd1(X):
	print "i get %r" % X
	return 5
	
print sd1(raw_input(">"))

#a = 30
#b = 5
#c = 78
#d = 4
#e = 90
#f = 2
#i = 100
#j = 2
	
#print "the puzzle is? %d" % (a+b+(c-d-i/j/2*e*f))

	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 
	
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b 
	
print subtract(add(24,divide(34,100)),1023)

