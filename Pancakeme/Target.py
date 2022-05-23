import random

class target:
    def __init__(self, n, target, numbers):
        self.n=n
        self.target=target
        self.numbers=numbers

    def calc(self):
        final = {}
        cnt=0
        for i in range(self.n):
            for j in range(self.n):
                if self.numbers[i] + self.numbers[j] == self.target and i != j:
                    cnt +=1
                    final[cnt] = [i, j]

        print(final)

numbers= [10,20,10,40,50,60,70]
first = target(7, 50, numbers)

first.calc()