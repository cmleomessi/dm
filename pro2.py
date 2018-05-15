import numpy as np
f =open( "iris.txt")
count=0
p=[0 for i in range(5)]
D= [[0]*4 for i in range(150)]

while True:
 lines=f.readline()
 if not lines:
     break
     pass
 count+=1
 p[0],p[1],p[2],p[3],p[4]=(lines.split(","))
 D[count-1][0]=float(p[0])
 D[count - 1][1] = float(p[1])
 D[count - 1][2] = float(p[2])
 D[count - 1][3] = float(p[3])
ans1= [[0]*150 for i in range(150)]
for i in range(150):
    for j in range(150):
        ans1[i][j]=(np.dot(D[i],D[j]))**2
ans=np.array(ans1)
print(ans)

D1= [[0]*10 for i in range(150)]
for i in range(150):
    D1[i][0]=D[i][0]**2
    D1[i][1]=D[i][1]**2
    D1[i][2] = D[i][2] ** 2
    D1[i][3] = D[i][3] ** 2
    D1[i][4] = 2**0.5*D[i][0]*D[i][1]
    D1[i][5] = 2** 0.5 * D[i][0] * D[i][2]
    D1[i][6] = 2 ** 0.5 * D[i][0] * D[i][3]
    D1[i][7] = 2 ** 0.5 * D[i][1] * D[i][2]
    D1[i][8] = 2 ** 0.5 * D[i][1] * D[i][3]
    D1[i][9] = 2 ** 0.5 * D[i][2] * D[i][3]
    D1=np.array(D1)
print(D1)    #第二题特征空间
sum0=[0 for i in range(4)]
for i in range(150):
    for j in range(4):
      sum0[j]+=D[i][j]

for i in range(4):
    sum0[i]/=150
DCenter= [[0]*4 for i in range(150)]
for i in range(150):
    for j in range(4):
        DCenter[i][j]=D[i][j]-sum0[j]
DCenter=np.array(DCenter)
print(DCenter)  #第二题中心化

sum1=[0 for i in range(4)]
Dnormolized= [[0]*4 for i in range(150)]
for i in range(150):
    for j in range(4):
        sum1[j]+=(D[i][j])**2

for i in range(150):
    for j in range(4):
        Dnormolized[i][j]=D[i][j]/sum1[j]
Dnormolized=np.array(Dnormolized)
print(Dnormolized)   #第二题归一化

Dm = np.array(D1)
kernel = np.zeros([count,count]) #核矩阵
for i in range(count):
    for j in range(count):
        kernel[i][j] = (np.dot(Dm[i], Dm[j]))
print(kernel)
print("结果和第一问中的结果一样")