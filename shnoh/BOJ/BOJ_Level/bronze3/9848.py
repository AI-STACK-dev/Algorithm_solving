import sys; input = sys.stdin.readline;
n, k = map(int, input().split())
pre = int(input())
cnt = 0
for _ in range(1, n):
    cur = int(input())
    if pre - k >= cur:
        cnt += 1
    pre = cur
print(cnt)