import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n, m, start = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

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
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
count = 0
max_time = -1
# print(graph)
for case in distance:
    if case == INF or case == 0:
        continue
    else:
        count +=1
        if case > max_time:
            max_time = case
print(count, max_time)