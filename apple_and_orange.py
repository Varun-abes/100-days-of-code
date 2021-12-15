s,t = input().split(" ")
s = int(s)
t = int(t)
a,b = input().split(" ")
a = int(a)
b = int(b)
m,n = input().split(" ")
m = int(m)
n = int(n)
apple_count = 0
orange_count = 0
apple = list(map(int,input().strip().split(" ")))
orange = list(map(int,input().strip().split(" ")))
for i in apple:
    if(a+i>=s and a+i<=t):
        apple_count+=1
for i in orange:
    if(b+i>=s and b+i<=t):
        orange_count+=1
print(apple_count)
print(orange_count)