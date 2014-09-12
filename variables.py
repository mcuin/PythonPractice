#!/urs/bin/python

counter = 100
miles = 1000.0
name = "John"

print counter
print miles
print name

a = b = c = 1
d, e, f = 1, 2, "John"

print a, b, c, d, e, f

var1 = 1
var2 = 10

print var1, var2

del var1

string = "Hello World!"

print string
print string[0]
print string[2:5]
print string[2:]
print string * 2
print string + "TEST"

list = ['abcd', 786, 2.23, 'john', 70.2]
tlist = [123, 'john']

print list
print list[0]
print list[1:3]
print list[2:]
print tlist * 2
print list + tlist

tuple = ('abcd', 786, 2.23, 'john', 70.2)
ttuple = (123, 'john')

print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print ttuple * 2
print tuple + ttuple

dictionary = {}
dictionary['one'] = "This is one."
dictionary[2] = "This is two."
tdictionary = {'name': 'john', 'code': 6734, 'name': 'john'}

print dictionary['one']
print dictionary[2]
print tdictionary
print tdictionary.keys()
print tdictionary.values()

