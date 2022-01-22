import sys;input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
MAX = int(1e9)
data = [[MAX]*(n) for _ in range(n)]
# data input
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    data[a-1][b-1] = 1
    data[b-1][a-1] = 1
# 자기자신은 0
for i in range(n):
    data[i][i] = 0

# 플로이드 와샬 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            data[i][j] = min(data[i][j] , data[i][k]+data[k][j])

ans = 0
vals = MAX
for i in range(n-1,-1,-1):
    val = sum(data[i])
    if val <= vals:
        vals = val
        ans = i
print(ans+1)