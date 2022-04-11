import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
distance = [INF] * (n+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost
dijkstra(1)
print(distance)
max_ = max(distance[1:])
idx = distance.index(max_)
print(idx, distance[idx], distance.count(max_))