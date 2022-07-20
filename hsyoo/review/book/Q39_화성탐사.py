import heapq
INF = int(1e9)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    n = int(input())
    board = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        board.append(temp)
    
    q = []
    distance = [[INF] * n for _ in range(n)]
    heapq.heappush(q, (board[0][0], 0, 0)) # cost, y, x
    distance[0][0] = board[0][0]

    while q:
        dist, y, x = heapq.heappop(q)
        if distance[y][x] < dist:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            cost = dist + board[ny][nx]
            if cost < distance[ny][nx]:
                heapq.heappush(q, (cost, ny, nx))
                distance[ny][nx] = cost
    
    print(distance[n-1][n-1])
        
    

