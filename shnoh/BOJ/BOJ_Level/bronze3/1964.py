import sys; input = sys.stdin.readline;
N = int(input())
# 1 + 4
# 1 + 4 + (4 + 3)
# 1 + 4 + (4 + 3) + (4 + 3 + 3)
# An = 1 + 4 * n + n *(n-1)// 2 * 3
res = 1 + 4 * N + 3 * N * (N - 1) // 2
print(res % 45678)