n = int(input())
res = []
for i in range(n):
    arr = list(map(int,input().strip().split(" ")))
    res.append(arr)
a = 0
b = 0
j = n-1
for i in range(n):
    a += res[i][i]
    b += res[i][j]
    j-=1
print(abs(a-b))