n = int(input())
s = 1
while s*(s+1)/2 <= n:
    s += 1
print(s-1)

