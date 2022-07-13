import heapq
from collections import defaultdict
INF = int(1e9)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))

case = defaultdict(int)

def dijkstra(graph, start):
    q = []
    heap = heapq.heappush(q, (0, start))
    distance = [INF] * (n+1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    for i in range(1, n+1):
        if start == i:
            continue
        else:
            if distance[i] != INF:
                case[start] +=1
                case[i] +=1
    
for i in range(1, n+1):
    dijkstra(graph, i)

cnt = 0
for key_ in case.keys():
    if case[key_] == n-1:
        cnt +=1

print(cnt)