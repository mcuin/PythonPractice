#!/usr/bin/python
import os

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

fo.close()

fo2 = open("foo.txt", "r+")
str = fo2.read(10);
print "Read string is: ", str

position = fo2.tell();
print "Current position is: ", position

fo2.close()

os.rename("foo.txt", "foo2.txt")
os.remove("foo2.txt")

os.mkdir("test")

 
