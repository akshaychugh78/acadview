#Question1

import pandas as pd
data= { 'Name':['AkshayChugh', 'Akshay'], 'Age':[21, 20], 'Mail id':['akshaychugh@gmail.com', 'akshay@gmail.com'], 'Phone Number':[0000000000, 1111111111] }
df = pd.DataFrame(data)
print (df)

#Question2

dff = pd.read_csv("weather.csv")
print("The first 5 rows are= ")
print (dff.head(5))

#Question3

print("The first 10 rows are= ")
print (dff.head(10))

#Question4

print('Basic Stats of entire data:\n',dff.describe(include='all'))

#Question5

print("The last 5 rows are= ")
print (dff.tail(5))

#Question5

print('Basic Stats of 2nd Coloumn:\n',dff.describe(include='all').Location)
