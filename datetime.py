#1/usr/bin/python

import time;

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970: ", ticks;

localtime = time.localtime(time.time())
print "Local current time: ", localtime;

localtime2 = time.asctime(time.localtime(time.time()))
print "Formatted time: ", localtime2;


