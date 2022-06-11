import sys; input = sys.stdin.readline;
n, m, k = map(int, input().split())
Min = min(n // 2, m)
n = n - 2 * Min
m = m - Min
k = max(k - n - m, 0)
print(int(Min - (k / 3)))