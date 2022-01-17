n=input()
ans = 0
for i,s in enumerate(n):
    if s.isalpha():
        s = 10 + (ord(s)-ord('A'))
    else:
        s = int(s)
    ans +=  s*16**(len(n)-1-i)
print(ans)