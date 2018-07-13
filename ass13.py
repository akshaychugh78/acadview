#question 1

a=3
if a<4:
    a=a/(a-3)
print(a)
print ("output:ZeroDivisionError occurs")

#Correction

a=3
try:
  if a<4:
    a=a/(a-3)
    print(a)

except ZeroDivisionError as ee:
  print("Error occured: ",ee)


#question 2

l=[1,2,3]
print(l[3])
print("output: IndexError will occur as list index  is out of range")

try:
  l=[1,2,3]
  print(l[3])

except IndexError as ee:
  print("Error occured: ",ee)


#question 3
 
try:
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    raise
print("output: An exception")
print("Output:An exception")
print("Traceback (most recent call last):")
print("File 'D:/Python Assignments/Exception Handling/1.py', line 2, in <module>")
print("raise NameError('Hi there')")
print("NameError: Hi there")

#question 4

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
output: -5.0
a/b result in 0
  
#question 5

#Import Error

l=[1,3,6,9]

try:
    for i in range(4):
       
        print("Factorial of %d"%(l[i]))
        print(math.factorial(l[i]))
        
except ImportError as impt:
    print("Import Error")
except :
    print("Error")
finally:
    print("Program executed")

#Value Error

try:
    n=int(input("Enter value"))

except ValueError as vee:
    print(vee)
except Exception as ee:
    print(ee)


#Index Error

l=[2,3,4]
try:
    for i in range(0,5):
        print(l[i])
except IndexError as ie:
    print(ie)



#question 6
    
class AgeTooSmall(Exception):
    def __init__(self):
        self.m="Age is less than 18"
    def show(self):
        print(self.m)
while True:
      try:
       n=int(input("enter your age"))  
    if(n<18):
       raise AgeTooSmall
except AgeTooSmall as aee:
    aee.show()

