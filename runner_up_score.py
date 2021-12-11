def is_maxx(arr):
    maxx = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>maxx):
            maxx = arr[i]
    return maxx
def runner_up(arr):
    ans = is_maxx(arr)
    lst = []
    for i in range(len(arr)):
        if (arr[i])!=ans:
            lst.append(arr[i])
    return(is_maxx(lst))
n = int(input())
arr = list(map(int,input().strip().split(" ")))
res = runner_up(arr)
print(res)