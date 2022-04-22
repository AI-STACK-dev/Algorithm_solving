def solution(board, moves):
    answer = 0
    list_ = []
    n = len(board)
    for move in moves:
        j = move
        for i in range(n):
            if board[i][j-1] != 0:
                print(f"board에서 만난 수 : {board[i][j-1]}")
                if len(list_) > 0 and list_[-1] != board[i][j-1]:
                    list_.append(board[i][j-1])
                    board[i][j-1] = 0
                    break
                elif len(list_) > 0 and list_[-1] == board[i][j-1]:
                    list_.pop()
                    answer += 1
                    board[i][j-1] = 0
                    break
                elif len(list_) == 0:
                    list_.append(board[i][j-1])
                    board[i][j-1] = 0
                    break
    answer *= 2
    return answer