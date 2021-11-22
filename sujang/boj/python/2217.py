import sys; input = sys.stdin.readline

n = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(n)]
data.sort()

ans = 0
for i in range(n):
    ans = max(ans,data[i]*(n-i))
print(ans)