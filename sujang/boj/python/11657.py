import sys;input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
data = []
for _ in range(m):
    a,b,c = map(int,input().rstrip().split())
    data.append([a,b,c])

INF = int(1e9)
distance = [INF] * (n+1)

def bellmanFord(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            a,b,c = data[j]
            if distance[a] != INF and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == n-1:
                    return True
    return False

if bellmanFord(1):
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
        