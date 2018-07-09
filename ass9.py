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

class MovieDetails:
def __init__(self,name,artist,year,ratings):
        self.name=name
        self.artist=artist
        self.year=year
        self.ratings=ratings
   
 	def display(self):
print("The",self.name,"starring",self.artist,"has been released in",self.year,"with the ratings",self.ratings)

    	def update(self):
        name = input("Enter movie name: ")
        self.name = name
        artist = input("Enter artist name: ")
        self.artist = artist
        year = input("Enter year of release: ")
        self.year = year
        ratings = input("Enter ratings: ")
        self.ratings = ratings
        print("The",self.name,"starring",self.artist,"has been released in",self.year,"with the ratings",self.ratings)

movie=MovieDetails('Welcome','Akshay Kumar',2005,8.0)
movie.display()
movie.update()



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

