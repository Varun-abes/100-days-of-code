n = int(input())
res = []
arr = []
a = 0
rem = 0
for i in range(n):
    a = int(input())
    arr.append(a)
for i in arr:
    rem = i%5
    if(i<38):
        res.append(i)
    else:
        if(5-rem>=3):
            res.append(i)
        else:
            res.append(i+(5-rem))
for i in res:
    print(i)