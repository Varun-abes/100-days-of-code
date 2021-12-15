s = input()
a = 0
res = s.split(":")
if('PM' in res[2]):
    if(res[0]=='12'):
        new = s[0:len(s)-2]
        print(new)
    else:
        a = int(res[0])+12
        new = str(a)+s[2:len(s)-2]
        print(new)
else:
    if(res[0]=='12'):
        res[0] = '00'
        new = ":".join(res)
        print(new[:len(new)-2])
    else:
        print(s[:len(s)-2])