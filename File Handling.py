#Question 1

with open("qwerty.txt",'r') as f:
    data=f.readlines()
    for line in data:
        print(line)
    l = len(data)
    n= int(input("Enter the value:"))
    if (n<=l):
        print(data[n:])
    else:
        print("Line Doesn't Exist in .txt file")



#Question 2

wordcount={}
with open('qwerty.txt','r+') as f:

    data = f.readlines()
    words=[]
    for line in data:
        words+=line.split()
        print(words,"\n")

    for k in words:
        if k in wordcount:
            wordcount[k] += 1
        else:
            wordcount[k] = 1

print(wordcount)
        
#Question 3

file=open("qwerty.txt",'r')
data=file.read()
print(data)
file2= open("open.txt",'r+')
file2.write(data)
file2.close()
file3=open("close.txt",'r')
abc=file3.read()
print(abc)
file3.close()
        
#Question 4

with open("qwerty.txt",'r') as file1, open('open.txt','r') as file2,open('close.txt','w') as file3:
    
    a=file1.readlines()
    b=file2.readlines()
    for line1,line2 in zip(a,b):
        line4=line1+line2
        file3.write(line4)

file4=open('close.txt','r')
print(file4.read())
file4.close()

        
#Question 5

with open('qwerty.txt','w') as f1:
    for i in range(10):
        z=int(input("enter 10 integers"))
        f1.write("%d "%z)

with open('qwerty.txt','r') as f2,open('openfile.txt','w') as f3:

    data=openfile.readlines()

    for nos in data:
        nums=nos.split()
    nums.sort()
    for word in nums:
        f3.write("%s "%word)

f3=open('qwerty.txt','r')
print(f3.read())
f3.close
    
f4=open('openfile.txt','r')
print(f4.read())
f4.close
