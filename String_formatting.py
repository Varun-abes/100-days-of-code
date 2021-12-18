n = int(input())
for i in range(1,n+1):
        print(str(i).rjust(len(str(bin(n)[2:])),' '),end=' ')
        print(str(oct(i))[2:].rjust(len(str(bin(n)[2:])),' '),end = ' ')
        print(str(hex(i))[2:].upper().rjust(len(str(bin(n)[2:])),' '),end=' ')
        print(str(bin(i))[2:].rjust(len(str(bin(n)[2:])),' '),end=' ')
        print()