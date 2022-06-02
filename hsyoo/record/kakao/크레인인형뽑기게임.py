def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for move in moves:
        list_ = [case[move-1] for case in board]
        for idx in range(n):
            if list_[idx] != 0:
                temp = list_[idx]
                board[idx][move-1] = 0
                if len(stack) > 0 and temp == stack[-1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(temp)
                break
        
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))