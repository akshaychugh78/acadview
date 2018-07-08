# question 1

print("We represent time in a way that’s easy for us to understand. However, Python stores it in tuples.")
print("These python tuples are made of nine numbers. Leap seconds are added to make up to Earth’s slowing rotation.")
print("When DST is 0, it isn’t applied. When it’s 1, it is applied. However, when it is -1, it is up to the library to determine that.")
print("This tuple has an equivalent struct_time structure.")

#question 2
import datetime
today = datetime.date.today()
print (today)


#question 3

import datetime
x = datetime.datetime.now()
print(x.month)


#question 4

import datetime
x = datetime.datetime.now()
print(x.day)


#question 5

import datetime

d = datetime.datetime(2021,1,11)
print(d.year,d.month,d.day)


#question 6

import time
print(time.localtime())

#question 7

import math
x = int(input("enter the number"))
print(math.factorial(x))


#question 8

import math
x=int(input("enter first number"))
y = int(input("enter second number"))
print(math.gcd(x,y))


# question 9

import os
print(os.getcwd())
print(os.environ)
