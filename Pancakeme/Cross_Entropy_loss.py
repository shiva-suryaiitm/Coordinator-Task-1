import random
import math

y = []
yy = []

sum=0

for i in range(100):
    n = random.randint(0,1)

    y.append(n)
    yy.append(random.random())

    sum += (y[i]*math.log2(yy[i])) + ((1-y[i])*math.log2(1-yy[i]))


for i in range(100):
    sum+= (y[i]*math.log2(yy[i])) + ((1-y[i])*math.log2(1-yy[i]))

O = -(1/100)*sum

print(O)
