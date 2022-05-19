# Time complexity = O(n^2)

import numpy as np
import pandas as pd

class coord_2:
    def __init__(self, low=0, high=100, tar=50, size=100):
        self.low = low
        self.high = high
        self.tar = tar
        self.size = size

    def listgen(self):

        low = self.low
        high = self.high
        size = self.size
        lis = np.random.randint(low, high, size=size)
        lis = list(x for x in lis if x < self.tar)
        return lis

    def Findsum(self):

        sumpairs = {}
        arr = self.listgen()
        keys = {-1}
        nums = []

        for j in arr:
            target = self.tar
            target -= j
            if target > 0 and j not in keys:
                for m in arr:
                    if m == target and m not in keys:
                        keys.add(m)
                        keys.add(j)
                        nums.append(f"{j} + {m}")
            sumpairs["pairs"] = nums

        return pd.DataFrame.from_dict(sumpairs)


n = coord_2()
L = n.Findsum()
print(L)



