N=int(input())
num=0
index=0
K= []

for i in range(0,N):
    num = int(input())
    K.append(num)
for j in range(1,N):
    for k in range(j,N,1):
        if (K[j-1]>K[k]): # 버블 정렬
            index=K[j-1]
            K[j-1]=K[k]
            K[k]=index
for k in range(N):
    print(K[k])


