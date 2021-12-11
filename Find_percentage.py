N = int(input())
dic = {}
ans = 0
for i in range(N):
    arr = list(input().strip().split(" "))
    dic[arr[0]] = arr[1:]
query = input()
for i in range(len(dic[query])):
    ans = ans+float(dic[query][i])
ans = ans/len(dic[query])
print("{:.2f}".format(ans))
