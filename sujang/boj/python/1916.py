import sys; input = sys.stdin.readline
import heapq as hp

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
start,dest = map(int,input().split())


distance = [int(1e9)]*(n+1)
def dijkstra(start):
    h = []
    hp.heappush(h,[0,start])
    distance[start] = 0
    while h:
        dis,nod = hp.heappop(h)
        if distance[nod] < dis:
            continue
        for c,b in graph[nod]:
            cost = dis + c
            if cost < distance[b]:
                distance[b] = cost
                hp.heappush(h,[cost,b])

dijkstra(start)
print(distance[dest])