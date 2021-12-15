s = input().lower()
sub = input().lower()
count = 0
for i in range(len(s)):
    if(s[i:].startswith(sub)):
        count+=1
print(count)