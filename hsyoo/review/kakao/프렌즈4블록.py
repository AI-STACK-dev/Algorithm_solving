def check_4block(n,m,board):
    unique = set()
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j].isalpha() and board[i][j+1].isalpha() and board[i+1][j].isalpha() and board[i+1][j+1].isalpha() and (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]):
                 unique.update([(i,j), (i, j+1), (i+1, j), (i+1, j+1)])

    for case in list(unique):
        board[case[0]][case[1]] = '0'
    return len(unique), board

def top_down(n, m, board):
    for j in range(m):
        col_list = [case[j] for case in board]
        new_list = [x for x in col_list if x != '0']
        new_list = ''.join(new_list)
        new_list = new_list.rjust(n, '0')

        for i in range(n):
            board[i][j] = new_list[i]
    return board

def solution(n, m, board):
    answer = 0 
    new_board = []
    for temp in board:
        new_board.append(list(temp))
    board = new_board

    while True:
        length, board = check_4block(n,m,board)
        if length == 0:
            return answer
        answer += length

        board = top_down(n, m, board)

print(solution(4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]	))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	))