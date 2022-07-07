n = int(input())
m = int(input())
distance = []
INF = int(1e9)
for _ in range(n+1):
    temp = [INF] * (n + 1)
    distance.append(temp)

for _ in range(m):
    a,b,c = map(int, input().split())
    if distance[a][b] == INF:
        distance[a][b] = c
    else:
        distance[a][b] = min(distance[a][b], c)
for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            distance[i][j] = 0
        print(distance[i][j], end = ' ')
    print()
    # if i !=0:
    #     print(distance[i][1:])

