import random as r
import math as m

y=[]
y1=[]
for i in range(1,101):
    y1.append(r.random())
    y.append(r.randint(0,1))
 # cross entropy function vector
o = 0
for i in range(0,100):
    o+=(-0.01)*(y[i]*(m.log2(y1[i])) + (1-y[i])*m.log2(1-y1[i]))

print(o) 