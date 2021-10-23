from sys import stdin
from collections import deque

# 입력
n = int(stdin.readline().rstrip())
x,y = map(int,stdin.readline().rstrip().split())
m = int(stdin.readline().rstrip())
graph =[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 방문 여부 파악 리스트
visited = [0]*(n+1)

def bfs(x,y):
    cnt = 0
    d = deque([(x,cnt)])
    visited[x] = 1
    while d:
        a,cnt = d.popleft()
        for b in graph[a]:
            if b == y:
                return cnt + 1
            if not visited[b]:
                visited[b] = 1
                d.append((b,cnt+1))
    return -1

print(bfs(x,y))