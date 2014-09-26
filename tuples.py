#!/usr/bin/python

tup1 = ('chemistry', 'physcis', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7);
tup3 = "a", "b", "c", "d";
typ4 = ();
tup5 = (50,);

print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

tup6 = (12, 34.56);
tup7 = ('abc', 'xyz');

tup8 = tup6 + tup7;

print "tup8: ", tup8;

del tup1

print "tup1 after delete: ", tup1;
