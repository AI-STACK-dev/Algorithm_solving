'''
문제 4. 
35분 소요
'''
from copy import deepcopy as dp
maxDiff = 0
maxBoard = []
# 라이언이 어피치보다 한 발 더 맞히거나, 아예 안 맞히는 경우 밖에 없다
def solution(n, info):
    def dfs(aScore, lScore, shotCount, idx, board):
        global maxDiff, maxBoard
        if shotCount > n:
            return
        if idx > 10:
            tempDiff = lScore - aScore
            if tempDiff > maxDiff:
                board[10] += n - shotCount
                maxBoard = board
                maxDiff = tempDiff
            return
        
        # 어피치보다 큰 점수 획득
        if shotCount < n:
            tempBoard = dp(board)
            tempBoard[10-idx] = info[10-idx] + 1
            dfs(aScore, lScore+idx, shotCount+tempBoard[10-idx], idx+1, tempBoard)
            
        tempBoard2 = dp(board)
        # 어피치만 맞춤
        if info[10-idx] > 0:
            dfs(aScore+idx, lScore, shotCount, idx+1, board)
        # 둘 다 못 맞춤
        else:
            dfs(aScore, lScore, shotCount, idx+1, board)
        
    dfs(0,0,0,0,[0]*11)
    
    if maxBoard:
        return maxBoard
    else:
        return [-1]