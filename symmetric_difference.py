M = int(input())
a = list(map(int,input().strip().split(" ")))
M = int(input())
b = list(map(int,input().strip().split(" ")))
lst =[]
new = []
dif_a = list(set(a).difference(set(b)))
dif_b = list(set(b).difference(set(a)))
lst.append(dif_a)
lst.append(dif_b)
for i in range(len(lst)):
    for j in range(len(lst[i])):
        new.append(lst[i][j])
new = sorted(new)
for i in range(len(new)):
    print(new[i])