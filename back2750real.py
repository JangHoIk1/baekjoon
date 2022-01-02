N=int(input())
num=0
index=0
K= []

for i in range(0,N,1):
    num = int(input())
    K.append(num)
print(K)
for j in range(1,N,1):
    for k in range(j,N,1):
        if (K[j-1]>K[k]):
            index=K[j-1]
            K[j-1]=K[k]
            K[k]=index
                        
print(K)

