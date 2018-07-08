#Question1

import numpy as np
import math
r = np.random.random((10,1))
print(r)
print(np.mean(r))

#Question2

i=np.random.random((20,1))
print (i)
print("Standard Deviation: ",(np.std(i)))

print("Variance: ",(np.var(i)))

#Question3

t = np.random.random((10,20))
h = np.random.random((20,25))
print(t)
print(h)
v= np.dot(t,h)
print(v)
print("Size: ",v.shape)

#Question4

k = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(k)
u = lambda x:( 1 / (1 + math.exp(-x)))
m = np.array(list(map(u,k)))
print("New array:  ",m)
print(m.shape)





                 

