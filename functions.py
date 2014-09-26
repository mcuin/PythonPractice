#!/urs/bin/python

def printme(str):
	"This prints a passed string into the function."
	print str;
	return;

printme("I'm first call to user defined function.")
printme("Again second call to same function.")

def changeMe(myList):
	myList.append([1, 2, 3, 4]);
	print "Values inside function: ", myList;
	return

myList = [10, 20, 30]
changeMe(myList)
print "Values outside my list: ", myList;

def printInfo(name, age = 35):
	print "Name: ", name;
	print "Age: ", age;
	return;

printInfo(age = 50, name = "Mikki");
printInfo(name = "Miki");

def printInfo2(arg1, *vartuple):
	print "Output: " 
	print arg1
	for var in vartuple:
		print var;
	return;

printInfo2(10);
printInfo2(70, 60, 50);

sum = lambda arg1, arg2: arg1 + arg2;

print "Value of total: ", sum(10, 10);
print "Value of total: ", sum(10, 20);

def sum(arg1, arg2):
	total = arg1 + arg2
	print "Inside the function: ", total
	return total;

total = sum(10, 20);
print "Outside function: ", total;

total2 = 0;
def sum2(arg1, arg2):
	total2 = arg1 + arg2
	print "Inside function: ", total2;
	return total2;

sum(10, 20) 
print "Outside function: ", total2 
