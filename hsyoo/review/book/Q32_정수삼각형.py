n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            left = -1
            right = graph[i-1][j]
        elif j == i:
            left = graph[i-1][j-1]
            right = -1
        else:
            left = graph[i-1][j-1]
            right = graph[i-1][j]
        graph[i][j] = max(graph[i][j] + left, graph[i][j] + right)
print(max(graph[n-1]))