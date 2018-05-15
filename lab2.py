import numpy as np
from math import e
from sklearn.cluster import DBSCAN
F=open( "iris1.txt")
E=0.0001   ## the tolerance for convergence
f=2       ##the minimum density
h=2      ##the bandwidth
A= set()
R= set()

p=[0 for i in range(5)]
D= [[0]*4 for i in range(150)]
D1= [[0]*4 for i in range(150)]
count=0
while True:
 lines=F.readline()
 if not lines:
     break
     pass
 count+=1
 p[0],p[1],p[2],p[3],p[4]=(lines.split(","))
 D[count-1][0]=float(p[0])
 D[count - 1][1] = float(p[1])
 D[count - 1][2] = float(p[2])
 D[count - 1][3] = float(p[3])

d=np.matrix(D)



def Findattractor(x,d,h,E):
   t=0
   X1=x
   sum1=0
   sum2=0
   while True:
        for i in range(0, count):
            temp1=X1-d[i]
            dist = np.linalg.norm(temp1)
            temp2=(-1*dist*dist)/(2*h*h)
            temp3=e**temp2
            temp4=temp3*X1
            sum1+=temp3
            sum2+=temp4
        X2=sum2/sum1
        temp5=X2-X1
        dist2 = np.linalg.norm(temp5)
        if dist2<=E:
            return X2
            break
        X1=X2
        pass

#print(Findattractor(d[1],d,h,E))

def fx(xi,h,dim,d):
    sum3=0
    for i in range(0, count):
        temp1 = xi - d[i]
        dist = np.linalg.norm(temp1)
        temp2 = (-1 * dist * dist) / (2 * h * h)
        temp3 = e ** temp2
        sum3+=temp3
    temp4 = sum3/(count*h**dim)
    return temp4




def DENCLUE(d,h,f,E):
    dic = {} #字典
    for i in range(0, count):
        x1=Findattractor(d[i],d,h,E)
        if fx(x1,h,4,d)>=f:
            A.add(d[i])
            if str(x1) not in dic.keys():
                temp=[]
                temp.append(d[i])
                dic[str[x1]]=temp
            else:
                temp=dic[str(x1)]
                temp.append(d[i])
                dic[str(x1)]=temp








