import sys; input = sys.stdin.readline
from collections import deque

m,n,k = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(k)]
field = [[0]*n  for _ in range(m)]

for b,a,d,c in area:
    for i in range(a,c):
        for j in range(b,d):
            field[i][j] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    q = deque([(a,b)])
    field[a][b] = 1
    area = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            x,y = a+dx[i],b+dy[i]
            if 0<=x<m and 0<=y<n and field[x][y] == 0:
                q.append((x,y))
                field[x][y] = 1
                area += 1
    return area

ans = 0
anslist = []
for i in range(m):
    for j in range(n):
        if field[i][j] == 0:
            anslist.append(bfs(i,j))
            ans += 1
            
print(ans)
anslist.sort()
print(*anslist, sep=' ')

