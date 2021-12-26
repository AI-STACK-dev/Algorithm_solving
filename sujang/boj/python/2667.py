import sys;input = sys.stdin.readline
from collections import deque

n = int(input())
data = [ list(map(int,list(input().rstrip()))) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(i,j,num):
    global n
    cnt = 1
    q = deque([[i,j]])
    data[i][j] = num
    while q:
        y,x = q.popleft()
        for i in range(4):
            a,b = x + dx[i], y + dy[i]
            if 0<=a<n and 0<=b<n and data[b][a] == 1:
                data[b][a] = num
                q.append([b,a])
                cnt +=1
    return cnt

num = 2
ans = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            ans.append(bfs(i,j,num))
            num += 1
ans.sort()
print(len(ans))
print(*ans,sep='\n')