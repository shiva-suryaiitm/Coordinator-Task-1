import numpy as np
import math

class coord1:

    def __init__(self, n):
        self.n = n

    def cross_entropy(self):
        g = self.n
        y = np.random.random(g)
        x = np.random.randint(2, size=g)

        return self.find_entropy(y, x)


    def find_entropy(self, y, x):
        epoch = self.n
        sums = 0
        for i in range(epoch):
            s1 = x[i]*math.log(y[i])
            s2 = (1-x[i])*math.log(1-y[i])
            sums = sums+s1+s2

        return (-1/epoch)*sums


n = int(input(" give your n value : "))
k = coord1(n)
entro = k.cross_entropy()
print(f'Entropy = {entro}')






