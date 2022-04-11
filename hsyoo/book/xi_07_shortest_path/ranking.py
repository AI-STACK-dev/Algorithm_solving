import sys
input = sys.stdin.readline
n,m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n+1)]
"""
초기화 해줘야한다. 자기 자신으로 가는 경우를
"""
for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1


for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

total = 0
for a in range(1,n+1):
    cnt = 0
    for b in range(1, n+1):
        if graph[a][b] != INF:
            cnt +=1
        if graph[b][a] != INF:
            cnt +=1
    if cnt >= (n-1):
        total += 1
print(total)