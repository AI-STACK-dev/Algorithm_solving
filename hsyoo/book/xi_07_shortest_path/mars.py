import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
T = int(input())



dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dijkstra(start):
    q = []
    heapq.heappush(q, (graph[start[0]][start[1]], start))
    distance[start[0]][start[1]] = graph[start[0]][start[1]]

    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            cost = dist + graph[ny][nx]
            if cost < distance[ny][nx]:
                distance[ny][nx] = cost
                heapq.heappush(q, (cost, (ny,nx)))

# dijkstra((0,0))
# print(distance)
for _ in range(T):
    n = int(input())
    graph =[list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    dijkstra((0,0))
    print(distance[n-1][n-1])
    
