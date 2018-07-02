# question 1

print("Create a list")
a=["Apple","Banana","Mango","Oragne","Kiwi"]
print (a)

# question 2

print("Adding Elements into list(INDEX VALUE)")
a=["Apple","Banana","Mango","Oragne","Kiwi"]
x=a.insert(0,"google")
x=a.insert(1,"apple")
x=a.insert(2,"facebook")
x=a.insert(3,"tesla")

print (a)

print ("Adding Elements into list(Append)")
b=["Apple","Banana","Mango","Oragne","Kiwi"]
x=b.append(['google', 'apple', 'facebook', 'tesla'])

print (b)

# question 3

a=["Apple","Banana","Mango","Oragne","Kiwi"]
print (a)
#x=a.insert(4,"Apple")
print (a)
a.count("Apple")

# question 4

a=[1,43,67,222,22,1,53]
print (a)
a.sort()
print("Sorted List")
print (a)

# question 5

a=[1,43,67,222,22,1,53]
b=[3,76,23,11,55,2221,36]
print(a,b)
print ("Sorted List a,b")
a.sort()
b.sort()
print (a,b)
print ("Merged List")
x=a+b
print (x)
print ("Sorted Merged List")
x.sort()
print (x)

# question 6
#problem in stack and queue

# question 7

a= [1,2,3,4,5,6,7,8,9,99,100]
print(a)

even=[i for i in a if i%2 != 0 ]
print("Even Numbers")

odd=[i for i in a if i%2 == 0]
print(odd) 
print("Odd Numbers")
print(even)
