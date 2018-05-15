import numpy as np
import math
import matplotlib.pyplot as plt
count=0
a=[0 for i in range(10)]
p=[0 for i in range(11)]

f =open( "magic04.txt")

while True:
 lines = f.readline()
 if not lines:
     break
 count+=1
 pass

D= [[0]*10 for i in range(count)]
count1=0
h =open( "magic04.txt")

while True:
 lines=h.readline()
 if not lines:
     break
     pass
 count1+=1
 p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10]=(lines.split(","))
 for i in range(0,10):
  D[count1 - 1][i] = float(p[i])
 for j in range(0,10):
  a[j]=a[j]+float(p[j])
  pass
d=np.matrix(D)
for p in range(0, 10):
  a[p]=a[p]/count
ut=np.matrix(a)
u = np.transpose(ut)
u=np.array(u)
print(u)                  #第一题

temp=[1 for i in range(count)]
tempmatrix=np.matrix(temp)
tempmatrixt = np.transpose(tempmatrix)
temp1=tempmatrixt*ut
z=d-temp1
zt=np.transpose(z)
inner=1/3*zt*z    #第二题
inner=np.array(inner)
print(inner)

Sum=0
temp2=0
ew=np.transpose(z[1])
zp=[0 for i in range(count)]
for i in range(count):
  zp[i]=np.transpose(z[i])
  temp2=zp[i]*z[i]
  Sum+=temp2
Sum=Sum/3
Sum=np.array(Sum)
print(Sum)  #第三题

import math
def pearson(vector1, vector2):
    n = len(vector1)
    sum1 = sum(float(vector1[i]) for i in range(n))
    sum2 = sum(float(vector2[i]) for i in range(n))
    sum1_pow = sum([pow(v, 2.0) for v in vector1])
    sum2_pow = sum([pow(v, 2.0) for v in vector2])
    p_sum = sum([vector1[i]*vector2[i] for i in range(n)])
    num = p_sum - (sum1*sum2/n)
    fenmu= math.sqrt((sum1_pow-pow(sum1, 2)/n)*(sum2_pow-pow(sum2, 2)/n))
    if fenmu == 0:
        return 0.0
    return num/fenmu

v1=[0 for i in range(count)]
v2=[0 for i in range(count)]
for i in range(count):
  v1[i]=D[i][0]
  v2[i]=D[i][1]
print(pearson(v1,v2))   #第四题
plt.scatter(v1,v2)
plt.show()


matrix = np.array(D)
mean = np.mean(matrix, axis=0)
vars = np.var(matrix, axis=0)
data = v1
def zhengtai(x):
    temp0=(x-mean[0])**2
    temp1=2*vars[0]
    temp2=2*np.pi*vars[0]
    p = np.exp(-temp0/temp1)/(np.sqrt(temp2))
    return p
x = np.linspace(mean[0] - 300, mean[0] + 300, 1000)
y = [zhengtai(i) for i in x]
plt.plot(x, y)
plt.show()     #第五题


DT=np.transpose(D)
variance=[0 for i in range(10)]
for i in range(10):
  narray=np.array(DT[i])
  Sum1=narray.sum()
  narray2=narray*narray
  Sum2=narray2.sum()
  mean=Sum1/count
  variance[i]=Sum2/count-mean**2
print(variance)                      #第六题
print("第十列方差最大,第五列方差最小")















