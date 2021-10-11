from sys import stdin
from bisect import bisect_left as BL

n = int(stdin.readline())
A = list(map(int,stdin.readline().split()))

num = [0]
i = 0
for a in A:
    if a > num[i]:
        num.append(a)
        i += 1
    else:
        idx = BL(num,a)
        num[idx] = a
print(len(num)-1)


