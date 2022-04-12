import sys; input = sys.stdin.readline;
n = int(input())
k = int(input()) + 60
if n < k:
    res = 1500 * n
else:
    res = k * 1500 + (n - k) * 3000
print(res)