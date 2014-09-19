#!/usr/bin/python

var1 = 'Hello World!'
var2 = 'Python programming'

print "var1[0]: ", var1[0]
print "var2[1:5] ", var2[1:5]

print "Updated string :- ", var1[:6] + 'Python' 

print "My name is %s and my weight is %d kg." % ('Zara', 21)

paraStr = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print paraStr

print r'C:\\nowhere'

print u'Hello World!'
