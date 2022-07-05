from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = int(1e9)
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
queue = deque([(x, 0)])
visited[x] = True
distance[x] = 0

while queue:
    now, cost = queue.popleft()
    for next in graph[now]:
        if visited[next] == False:
            queue.append((next, cost + 1))
            visited[next] = True
            distance[next] = cost + 1

flag = True
for i in range(1, n+1):
    if visited[i] == True and distance[i] == k:
        flag = False
        print(i)
if flag == True:
    print(-1)

