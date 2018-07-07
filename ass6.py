# question 1

x=[input("Enter the values:")for i in range(10)]
print (x)

# question 2

while True:
  print ("cool")
			
# question 3

l1 = []
for x in range (5):
    y = int(input("enter the values"))
    l1.append(y)
print(l1)
l2=[]
for x in l1:
    z=x*x
    l2.append(z)
print(l2)

# question 4

a=[1,2,3.0,4.0,"a","b"]
b=[]
c=[]
d=[]

for i in a:
  if type(i)==str:
    b.append(i)
  elif type(i)==float:
    c.append(i)
  else:
    d.append(i)
print (b)
print (c)
print (d)

# question 5

b=[]
c=[]
for i in range(1,101):
  if i%2==0:
    b.append(i)
  if i%2==1:
    c.append(i)
print (b)
print (c)

# question 6

print ("Pattern ")
for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()

# question 7

dict ={}
for i in range(5):
    name = input("Enter Name:")
    marks = int (input("Enter Marks:"))
    dict[name] = marks
print (dict)


