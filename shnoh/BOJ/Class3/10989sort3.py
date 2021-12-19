import sys; input = sys.stdin.readline
res = [0] * 10000
n = int(input().rstrip())
for _ in range(n):
    k = int(input().rstrip())
    res[k - 1] += 1
for i in range(10000):
    for _ in range(res[i]):
        print(i + 1)