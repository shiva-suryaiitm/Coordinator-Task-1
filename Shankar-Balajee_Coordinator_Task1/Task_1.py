
import numpy as np
import pandas
import math
n=100
list_1=np.random.randint(0,2,(n,1))
list_2=np.random.rand(n)
sum=0.00
for i in range(n):
    expression=list_1[i]*math.log2(list_2[i])
    expression+=(1-list_1[i])*math.log2(1-list_2[i])
    sum+=expression
sum= (-0.01)*sum
print(sum.item())