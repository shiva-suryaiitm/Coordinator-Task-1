l=[10,20,10,40,50,60,70]
target=50
class timepass():
    def __init__(self):
        self.dict={}
    def solve(self,l,target):
        self.l=l
        self.target=target
        self.length=len(l)
        c=1
        for i in range(self.length):
            for j in range(self.length):
                m=[]
                if(l[i]+l[j]==self.target):
                    m.append(i)
                    m.append(j)
                    self.dict[c]=m
                    c+=1
        return self.dict

lol=timepass()
answer=lol.solve(l,target)  
print(answer)   
