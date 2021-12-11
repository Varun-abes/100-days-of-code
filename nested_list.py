def second_lowest(arr):
    lst1 = []
    lst2 = []
    i = 0
    maxx = arr[i][1]
    minn = -99999
    for i in range(len(arr)):
        if(arr[i][1]<maxx):
            maxx = arr[i][1]
    #print(maxx)
    for i in range(len(arr)):
        #print(arr[i][1])
        if(arr[i][1]!=maxx):
            lst1.append(arr[i][1])
    #print(lst1)
    minn = min(lst1)
    for i in range(len(arr)) :
        if(arr[i][1]==minn):
            lst2.append(arr[i][0])
    return sorted(lst2)
N = int(input())
arr = []
for i in range(N):
    lst= []
    #arr = []
    name = input()
    num = float(input())
    lst.append(name)
    lst.append(num)
    arr.append(lst)
ans = second_lowest(arr)
for i in range(len(ans)):
    print(ans[i])