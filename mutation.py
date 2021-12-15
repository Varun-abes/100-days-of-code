s = input()
pos, ch = input().split(" ")
pos = int(pos)
print(s[0:pos]+ch+s[pos+1:])