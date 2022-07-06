t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr = []
    graph = []
    for _ in range(n):
        tmp = [0] * m
        arr.append(tmp)
        tmp2 = [0] * m
        graph.append(tmp2)

    temp = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(m):
            arr[i][j] = temp[cnt]
            if j == 0:
                graph[i][j] = arr[i][j]
            cnt +=1
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                graph[i][j] = max(graph[i][j-1] + arr[i][j], graph[i+1][j] + arr[i][j])
            elif i == n-1:
                graph[i][j] = max(graph[i-1][j-1] + arr[i][j], graph[i][j-1] + arr[i][j])
            else:
                graph[i][j] = max(graph[i-1][j-1] + arr[i][j], graph[i][j-1] + arr[i][j], graph[i+1][j-1] + arr[i][j])
    list_ = [item[-1] for item in graph]
    print(max(list_))
    

    
        