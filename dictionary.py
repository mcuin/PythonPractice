#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict2 = {'abc': 456};
dict3 = {'abc': 123, 98.6: 37};

print "dict[Name]: ", dict['Name'];
print "dict[Age]: ", dict['Age'];

dict['Age'] = 8;
dict['School'] = "DPS School";

print "dict[Age]: ", dict['Age'];
print "dict[School]: ", dict['School'];

del dict['Name'];
dict.clear();
del dict;
