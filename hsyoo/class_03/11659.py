import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
ary = list(map(int, input().rstrip().split()))
prefix_sum = [0] * n
result = 0
for i in range(n):
    prefix_sum[i] = result + ary[i]
    result += ary[i]
for _ in range(m):
    l_i, r_i = map(int, input().rstrip().split())
    l_i, r_i = l_i - 1, r_i - 1
    # 0, 2일 때,
    print(prefix_sum[r_i] - prefix_sum[l_i] + ary[l_i])