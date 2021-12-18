s = input()
k = int(input())
n = len(s)
for i in range(0,n,k):
    ans = ''
    for j in s[i:i+k]:
        if(j not in ans):
           ans = ans+j
    print(ans)