import sys; input = sys.stdin.readline;
n, k = map(int, input().split())
data = []
for i in range(1, n + 1):
    if n % i == 0:
        data.append(i)
Len = len(data)
if Len < k:
    print(0)
else:
    print(data[k - 1])