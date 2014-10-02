#!/usr/bin/python

str = raw_input("Enter your input: ");
print "Recieved input is: ", str

str = input("Enter your input: ");
print "Recieved input is: ", str

fo = open("foo.txt", "wb") 
print "Name of the file: ", fo.name
print "Closed or not:" , fo.closed
print "Opening mode: ", fo.mode
print "Softspace flag: ", fo.softspace

fo.write("Python is a great languages.\nYeah it's great!\n");

str = fo.read(10);
print "Read string is: ", str

position = fo.tell();
print "Current position is: ", position

fo.close()

 
