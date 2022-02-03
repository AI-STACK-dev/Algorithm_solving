import sys; input=sys.stdin.readline
import heapq as hp
INF = int(1e9)


v,e = map(int,input().rstrip().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().rstrip().split())
    graph[a].append((b,c))
distance = [INF]*(v+1)

def dijkstra(start):
    q = []
    hp.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis,now = hp.heappop(q)
        if distance[now] < dis:
            continue
        for i in graph[now]:
            cost = dis+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hp.heappush(q,(cost,i[0]))
dijkstra(start)
for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
