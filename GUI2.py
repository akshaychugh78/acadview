#Question 1

from tkinter import *

root=Tk()
root.title("User List")
root.geometry('400x400')

data={'akshay':'0000000000','chugh':'1111111111','kumar':'2222222222','New':'3333333333'}

f12=Frame(root)    
f12.pack()

sb=Scrollbar(f12)
sb.pack(side=RIGHT, fill=Y)

listL=Listbox(f12,yscrollcommand=sb.set)

for i in data:
   listL.insert(END,i)

listL.pack(side=LEFT, fill=X)
sb.configure(command=listL.yview)
Button(root,text="Exit",fg="blue",bg="red",command=root.destroy).pack()
root.mainloop()

#Question 2

from tkinter import *

root=Tk()
root.title("Airtel User List!")
root.geometry('250x240')

data={'akshay':'0000000000','chugh':'1111111111','kumar':'2222222222','New':'3333333333'}

f1=Frame(root)    
f1.pack()

sb=Scrollbar(f1)
sb.pack(side=RIGHT, fill=Y)

listL=Listbox(f1,yscrollcommand=sb.set)

for i in data:
   listL.insert(END,i)

listL.pack(side=LEFT, fill=X)
sb.configure(command=listL.yview)


def addval():
     data[k.get()]=v.get()
     listL.insert(END,k.get())


f=Frame(root)
f.pack()
labelL=Label(f,text="Name ")
labelL.grid(row=0, column=0)
labelL=Label(f,text="Mobile No.")
labelL.grid(row=1,column=0)

k=Entry(f)
k.grid(row=0,column=1)
v=Entry(f)
v.grid(row=1,column=1)


b=Button(f,text="Add in Dictionary",command=addval)
b.grid(row=2,column=1)

root.mainloop()
