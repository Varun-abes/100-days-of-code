def sum_of_distinct(arr):
    lst = set(arr)
    n = len(lst)
    summ = 0
    for i in lst:
        summ+=i
    return summ/n
n = int(input())
ans = sum_of_distinct(list(map(int,input().strip().split(" "))))
print("Sum of dustinct values is ",ans)