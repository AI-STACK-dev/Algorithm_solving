dx,dy = [1,-1,0,0],[0,0,1,-1]

def cantMove(board,x,y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] == 1:
            return False
    return True
        
def dfs(board,x,y,z,k):
    if cantMove(board,x,y):
        return (False, 0)
    if x==z and y==k:
        return (True, 1)
    
    result = False
    minTurn, maxTurn = int(1e9), 0
    
    board[x][y] = 0
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] == 1:
            resultBool, resultCnt = dfs(board,z,k,nx,ny)
            if not resultBool:
                result = True
                minTurn = min(minTurn, resultCnt)
            elif not result:
                maxTurn = max(maxTurn, resultCnt)
    board[x][y] = 1
    turn = minTurn if result else maxTurn
    return result,turn+1
            
def solution(board, aloc, bloc):
    return dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]