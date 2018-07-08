# queston 1

class Circle():
   
   def __init__(self,r):
      self.radius = r
      
   def getArea(self):
      return(3.14*self.radius*self.radius)
     
   def getCircumference(self):
      return(2*3.14*self.radius)

x = Circle(4)
print("Area: ", x.getArea())
print("Circumference: ", x.getCircumference())


#question 2

class Student():

   def __init__(self,n,r):
      self.name = n
      self.roll_no = r

   def display(self):
      print("Name: ",self.name)
      print("Roll no: ",self.roll_no)

x = Student('akshay',67)
x.display()

#question 3

class Temperature():

   def __init__(self,c,f):
      self.celsius = c
      self.fahrenheit = f

   def convertFahrenheit(self):
      return(self.celsius*1.8+32)

   def convertCelsius(self):
      return((self.fahrenheit-32)/1.8)

x = Temperature(54,28)
print("Fahrenheit from Celsius: ", x.convertFahrenheit())

print("Celsius from Fahrenheit: ", x.convertCelsius())

#question 4

class Student():

    def __init__(self,n,m,rn,y): 
      self.name = n
      self.marks = m
      self.roll_no = rn
      self.year = y

    def details(self):
        print("name is:" , self.name)
        print("marks are:" , self.marks)
        print("roll no. is:" , self.roll_no)
        print("year :" , self.year)

    def address(self,val):
      self.address = val
      print("address is:" , self.address)

x = Student('akshay',11,67,2018)
x.details()
x.address('lado sarai')


#question 5


class Expenditure():

   def __init__(self,e,s):
      self.expenditure = e
      self.savings = s

   def display(self):
      print("Expenditure: ", self.expenditure)
      print("Savings: ",self.savings)

   def calc(self):
      self.total_salary = self.expenditure+self.savings

   def displaySalary(self):
      print("Total salary: ",self.total_salary)
      
x = Expenditure(40000,30000)
x.display()
x.calc()
x.displaySalary()

