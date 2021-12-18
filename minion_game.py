s = input().lower()
vowels = ['a','e','i','o','u']
stuart = 0
kevin = 0
for i in range(len(s)):
    if(s[i] in vowels):
        kevin = kevin+(len(s)-i)
    else:
        stuart = stuart + (len(s)-i)
if(stuart>kevin):
    print("Stuart",stuart)
else:
    print("Kevin",kevin)