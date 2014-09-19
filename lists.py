#!/bin/usr/python

list1 = ['physics', 'chemistry', 1997, 2001]
list2 = [1, 2, 3, 4, 5, 6]
list3 = ["a", "b", "c", "d"]

print "list1[0] ", list1[0]
print "list2[1:5] ", list2[1:5] 

print "Value at index 2 is: ", list1[2]
list1[2] = 2000
print "Value at index 2 is: ", list1[2]

print list1
del list1[3]
print list1
