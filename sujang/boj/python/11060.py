import sys; input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

ans = [int(1e9)] * 1101
ans[0] = 0
for i in range(n):
    for j in range(1, data[i]+1):
        ans[i+j] = min(ans[i]+1, ans[i+j])


if ans[n-1] < int(1e9):
    print(ans[n-1])
else:
    print(-1)
