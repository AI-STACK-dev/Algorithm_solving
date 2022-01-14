import sys; input = sys.stdin.readline;
L = int(input())
data = list(map(int, input().split()))
data.sort()
n = int(input())
for i in range(L):
    if data[i] < n and data[i + 1] > n:
        k = max(data[i + 1] - n, n - data[i])
