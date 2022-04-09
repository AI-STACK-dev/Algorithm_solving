import sys
import heapq

INF = int(1e8)
n,m,k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [[INF] * (n+1) for _ in range(n+1)]

def dijkstra(start):
    q = []
    cnt = 0
    heapq.heappush(q, (0, start, cnt))
    distance[start][cnt] = 0
    while q:
        dist, now, cnt = heapq.heappop(q)
        if distance[now][cnt] < dist:
            continue
        for next_, value in graph[now]:
            cost = distance[now][cnt] + value
            if cost < distance[next_][cnt]:
                distance[next_][cnt] = cost
                heapq.heappush(q, (value, next_, cnt))
            
            if cnt < k and distance[next_][cnt+1] > dist:
                distance[next_][cnt+1] = dist
                heapq.heappush(q, (dist, next_, cnt+1))
dijkstra(1)
# print(distance)
print(min(distance[n]))