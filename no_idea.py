n,m =input().split(" ")
arr = list(map(int,input().strip().split(" ")))
a = set(list(map(int,input().strip().split(" "))))
b = set(list(map(int,input().strip().split(" "))))
count = 0
for i in arr:
    if(i in a and i not in b):
        count+=1
    elif(i in b and i not in a):
        count-=1
print(count)