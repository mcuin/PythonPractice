#!/urs/bin/python

try:
	fh = open("testfile", "w")
	fh.write("This is my test file for exception handling!")
except IOError:
	print "Error: Can\'t find file or read data."
else:
	print "File write was successful."
	fh.close()

try:
	fh2 = open("testfile", "r")
	fh2.write("This is my test for exception handling!")
except IOError:
	print "Error: Can\'t find file or read data."
else:
	print "File write was successful."
	fh2.close()

try:
	fh3 = open("testfile", "w")
	fh3.write("This is my test for exception hnadling!")
finally:
	print "Error: Can\'t find file or read data."

try:
	fh4 = open("testfile", "w")
	try:
		fh4.write("This is my file for exception handling!")
	finally:
		print "Going to close file."
		fh4.close()
except IOError:
	print "Error: Can\'t find file or read data."
	
def temp_convert(var):
	try:
		return int(var)
	except ValueError, Argument:
		print "The argument does not contain numbers\n", Argument

temp_convert("xyz");
