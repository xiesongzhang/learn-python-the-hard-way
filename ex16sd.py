from sys import argv

script, filename = argv

file = open(filename)

print "Here is the new file %r:" % filename
print file.read()

