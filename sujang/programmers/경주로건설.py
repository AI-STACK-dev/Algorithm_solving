from collections import deque

def solution(board):
    n = len(board)
    q = deque([(0,0,-1,0)])
    costTable = [[[-1]*n for _ in range(n)] for _ in range(4)]
    costTable[0][0][0] = costTable[1][0][0] = costTable[2][0][0] = costTable[3][0][0] = 0
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    answer = int(1e9)
    while q:
        y,x,direction,cost = q.popleft()
        
        if y == n-1 and x == n-1:
            answer = min(answer, cost)
        
        for i in range(4):
            Y,X = y+dy[i],x+dx[i]
            if 0<=Y<n and 0<=X<n and board[Y][X] == 0:
                if direction == i or direction == -1:
                    cost_ = cost + 100
                else:
                    cost_ = cost + 600
                if costTable[i][Y][X] == -1 or costTable[i][Y][X] > cost_:
                    q.append((Y,X,i,cost_))
                    costTable[i][Y][X] = cost_
    return answer