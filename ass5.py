#question 1

year=(int(input("Enter The year to check its leap year or not:")))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("%d is a leap year" %year)
        else:
            print("%d is not a leap year" %year)
    else:
        print("%d is a leap year" %year)
else:
    print("%d is not a leap year" %year)

#question 2

L=(input("Enter The Length:"))
B=(input("Enter The Breath:"))
print (L,B)
if L==B:
    print ("It is a square Dimensions")
else:
    print ("It is a Rectangle Dimensions")


#question 3

A=(input("Enter The Age of First Person:"))
B=(input("Enter The Age of Second Person:"))
C=(input("Enter The Age of Third Person:"))

if A>B and A>C:
    print ("A is oldest Person")
elif B>A and B>C:
    print ("B is oldest Person")
else:
    print ("C is oldest Person")

#question 4

input("Enter the competitor Name:")
a=int(input("Enter the competitor scored:"))
if (a> 0 and a<=50):
    print("Sorry! No prize this time.")
elif (a>= 51 and a<=100):
    print("Congratulations! You won a Wooden Dog")
elif (a>=101 and a<=180):
    print("Congratulations! You won a Book")
elif (a>= 181 and a<=200):
    print("Congratulations! You won a Chocolates")
else :
    print("Sorry! No prize this time.")

#question 5

quantity = int(input("Enter the Quantity:"))
cost = quantity * 100

if (cost > 1000):
    print ("Discount of 10%")
    discount = (cost*10)/100
    update=cost-discount
    print (update)
    
else :
    print ("Billing : %d" %(cost))
