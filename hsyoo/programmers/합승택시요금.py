def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (n+1) for i in range(n+1)]
    # distance = [[INF] * (n+1) for i in range(n+1)]
    for fare in fares:
        i,j,cost = fare
        graph[i][j] = cost
        graph[j][i] = cost
    
    for k in range(1, n+1):
        for i in range(1, n+1): 
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    """
    case 1: 둘이서 특정 노드를 거친 후, 따로 가는 경우
    case 2: 둘이서 아예 따로따로 가는 경우
    case 3: 둘 중 한 명의 집을 들렀다가, 한명이 자기 집으로 가는 경우
    """
    case1 = INF
    for i in range(1, n+1):
        case1 = min(case1, graph[s][i] + graph[i][a] + graph[i][b])
    case2 = graph[s][a] + graph[s][b]
    case3 = min(graph[s][a] + graph[a][b], graph[s][b] + graph[b][a])
    answer = min(case1, case2, case3)

    return answer

# print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	))
# print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	))