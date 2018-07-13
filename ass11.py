#Question 1

import time
import threading

def task():
   print("Wait for 5 seconds")
   time.sleep(5)
   print("Hello")

threading.Thread(target=task).start()



#Question 2

import time
import threading

def task():
   for i in range(1,10):
      print(i)
      time.sleep(1)

threading.Thread(target=task).start()



#Question 3

import time
import threading

l=[1,2,3,4,5]

def task():
   de=2
   for i in l:
      print(i)
      time.sleep(de)
      de=de+2

threading.Thread(target=task).start()



#Question 4

import time
import threading
def fact(num,d):
    a=1
    for i in range(2,num+1):
       a*=i
    time.sleep(d)
    print("Factorial of %d is %d"%(num,a))

n=int(input("Enter number: "))
threading.Thread(target=fact,args=(n,2)).start()
