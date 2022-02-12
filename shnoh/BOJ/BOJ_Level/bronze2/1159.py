import sys; input = sys.stdin.readline;
from collections import Counter
n = int(input())
data = [input().rstrip() for _ in range(n)]
data2 = []
for name in data:
    data2.append(name[0])
counter = dict(Counter(data2))
data3 = []
for x in counter:
    if counter[x] >= 5:
        data3.append(x)
if data3:
    data3.sort()
    print(*data3, sep = "")
else:
    print("PREDAJA")