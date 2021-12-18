n = int(input())
lst = list(map(chr, range(97,123)))
mid = '-'.join(lst[n-1::-1]+lst[1:n])
m = len(mid)
for i in range(1,n):
    print('-'.join(lst[n-1:n-i:-1]+lst[n-i:n]).center(m,'-'))
print(mid)
for i in range(n-1,0,-1):
    print('-'.join(lst[n-1:n-i:-1]+lst[n-i:n]).center(m,'-'))