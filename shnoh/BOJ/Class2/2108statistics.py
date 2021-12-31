import sys; input = sys.stdin.readline;
from collections import Counter
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

print(round(sum(data) / n))
data.sort()
print(data[n // 2])
counter = Counter(data).most_common(2)
if n > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(counter[0][0])
print(data[n - 1] - data[0])