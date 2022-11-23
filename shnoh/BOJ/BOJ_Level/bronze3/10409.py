import sys; input = sys.stdin.readline;
n, T = map(int, input().split())
data = list(map(int, input().split()))
res = 0
for k in data:
    T -= k
    if T < 0:
        break
    res += 1
print(res)