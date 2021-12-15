s = input()
res = ""
for i in s:
    if(i.isupper()):
        res+=i.lower()
    else:
        res+=i.upper()
print(res)