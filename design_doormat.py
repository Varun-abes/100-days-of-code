n, m = input().split(" ")
n = int(n)
m = int(m)
a = '.|.'
for i in range(n//2):
    print((a*(2*i+1)).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(n//2,0,-1):
    print((a*(2*i-1)).center(m,'-'))