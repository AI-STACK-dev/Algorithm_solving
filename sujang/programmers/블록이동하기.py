from collections import deque

dy,dx = [1,-1,0,0], [0,0,1,-1]

def returnPossibleMoveCoord(board,y1,x1,y2,x2):
    n = len(board)
    result = []
    for i in range(4):
        ny1,ny2 = y1+dy[i], y2+dy[i]
        nx1,nx2 = x1+dx[i], x2+dx[i]
        if 0<=ny1<n and 0<=nx1<n and 0<=ny2<n and 0<=nx2<n:
            if board[ny1][nx1] ==0 and board[ny2][nx2] == 0:
                result.append(((ny1,nx1),(ny2,nx2)))
    
    # rotation
    if y1 != y2:
        param = [(0,1),(0,-1)]
    else:
        param = [(1,0),(-1,0)]
    
    for p in param:
        ny1,ny2 = y1+p[0], y2+p[0]
        nx1,nx2 = x1+p[1], x2+p[1]
        if 0<=ny1<n and 0<=nx1<n and 0<=ny2<n and 0<=nx2<n:
            if board[ny1][nx1] ==0 and board[ny2][nx2] == 0:
                result.append(((y1,x1),(y1+p[0],x1+p[1])))
                result.append(((y2,x2),(y2+p[0],x2+p[1])))
                
    return result
        
def solution(board):
    n = len(board)
    
    a,b = (0,0), (0,1)
    visited = set(((a,b)))
    q = deque([(a,b,0)])
    while q:
        a,b,cnt = q.popleft()
        for a_,b_ in returnPossibleMoveCoord(board,*a,*b):
            if (n-1,n-1) in [a_,b_]:
                return cnt+1
            if (a_,b_) not in visited:
                visited.add((a_,b_))
                q.append((a_,b_,cnt+1))