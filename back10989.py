N = int(input())
num = 0
K = []
change = 0
indexmin = 0
for i in range(N):
    num = int(input())
    K.append(num)

for j in range(0, N):  # j = 0 1 2 3 4
    indexmin = j  #
    for k in range(j + 1, N, 1):  # k= 1 2 3 4
        if (K[indexmin] > K[k]):
            indexmin = k
    print("hello")
    change = K[indexmin]
    K[indexmin] = K[j]
    K[j] = change
    print(K[j])
