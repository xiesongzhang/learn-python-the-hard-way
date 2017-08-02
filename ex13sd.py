from sys import argv

script, first,second = argv

print "i am:", first
print "you are:", second

age = raw_input("how old are you?")
age1 = raw_input("how old is she?")

print "So,you are %r ,she is %r ." % (
age,age1)
