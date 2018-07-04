#TUPLES
#question 1

language=("C","C#","PHP","Python")
Num=(11,22.56,33,44.0)
print (language)
print (Num)
a=(language + Num)
print (a)
print (len(a))

#question 2

Num=(11,22.56,22,44.0)
print (Num)
print ("Maximum Value",max(Num))
print ("Minmum Value",min(Num))

#question 3

Num=(11,22.56,22,44.0)
x=1
print (Num)
for i in Num:
    x=x*i
    i=i+1
print (x)

#SETS
#question 1

x={input("Enter the values in sets:")for i in range(5)}
print (x)
y={input("Enter the values in sets:")for i in range(5)}
print (y)
print ("Difference")
print("y-x")
a=y-x
print (a)
print("x-y")
a=x-y
print (a)
print ("Inter-section")
p=x&y
print (p)

#DICTIONARY
#question 1

dict ={}
for i in range(2):
    name = input("Enter Name:")
    marks = int (input("Enter Marks:"))
    dict[name] = marks
print (dict)

#question 2

dict1 = sorted(dict.items(), key=lambda x:x[1])
print (dict1)

#question 3

dict = {}
str = "MISSISSPPI"
m=str.count('M')
i=str.count('I')
s=str.count('S')
p=str.count('P')

dict['M']=m
dict['I']=i
dict['S']=s
dict['P']=p
print (dict)
