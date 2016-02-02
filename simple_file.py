#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name

print "new Line"

print "Closed or not : ", fo.closed
print "Softspace flag : ", fo.softspace
