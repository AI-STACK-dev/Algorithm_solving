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

x, k = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0,start))
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
    # print(distance)
    return distance[end]

a = dijkstra(1, k)
b = dijkstra(k, x)
total = a + b 
if total > INF:
    print(-1)
else:
    print(total)

    
