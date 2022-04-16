from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
ary = []
sum = 0
for _ in range(n):
    ary.append(int(input()))
    sum += ary[-1]

ary.sort()
print(round(sum/n))
print(ary[n//2])
c = Counter(ary)
mode, value = c.most_common()[0]
modes = [key for key in c.keys() if c[key] == value]
modes.sort()
if len(modes) != 1:
    print(modes[1])
else:
    print(mode)
print(ary[-1] - ary[0])
