import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(graph, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra(graph, start, distance)

for i in range(1,n+1):
    if i == start:
        print(0)
    else:
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])
