import heapq

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
INF = int(1e9)
start = 1
distance = [INF] * (n + 1)
distance[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next, next_cost in graph[now]:
        cost = dist + next_cost
        if cost < distance[next]:
            heapq.heappush(q, (cost, next))
            distance[next] = cost

max_ = max(distance[1:])
min_max = -1
for i in range(1, n+1):
    if min_max == -1 and distance[i] == max_:
        min_max = i
print(min_max, max_, distance[1:].count(max_))
