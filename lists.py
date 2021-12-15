dic = {}
dic[1] = 'insert'
dic[2] = 'print'
dic[3] = 'remove'
dic[4] = 'append'
dic[5] = 'sort'
dic[6] = 'pop'
dic[7] = 'reverse'
res = []
N = int(input())
for i in range(N):
    arr = list(input().strip().split(" "))
    if(arr[0] == dic[1]):
        res.insert(int(arr[1]),int(arr[2]))
    elif(arr[0] == dic[2]):
        print(res)
    elif(arr[0] == dic[3]):
        res.remove(int(arr[1]))
    elif(arr[0] == dic[4]):
        res.append(int(arr[1]))
    elif(arr[0] == dic[5]):
        res.sort()
    elif(arr[0] == dic[6]):
        res.pop()
    else:
        res.reverse()