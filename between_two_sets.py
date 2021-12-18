n, m = input().split(" ")
n = int(n)
m = int(m)
a = list(map(int,input().strip().split(" ")))
b = list(map(int,input().strip().split(" ")))
res = 0
factor = True
for i in range(max(a),min(b)+1):
    factor = True
    for j in a:
        if(i%j!=0):
            factor = False
            break
    for k in b:
        if(k%i!=0):
            factor = False
            break
    if(factor==True):
        res+=1
print(res)