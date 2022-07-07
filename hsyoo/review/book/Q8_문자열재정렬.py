s = list(input())
l1 = []
l2 = []
for c in s:
    if c.isalpha():
        l1.append(c)
    else:
        l2.append(int(c))
l1.sort()
s1 = ''.join(l1)
print(s1 + str(sum(l2)))       
