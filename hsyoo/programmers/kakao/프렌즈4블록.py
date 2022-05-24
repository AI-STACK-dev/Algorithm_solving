def scoring(m,n,board, score):
    """
    숫자형태로 제공받은 board(1 ~ 8까지)를 가지고 진행.
    만약 2X2가 완성되면 stack에 좌표를 넣는다. 그 후 중복을 제거하고 싶으면 set연산을 진행하여 
    set의 길이만큼을 score에 더해준다.
    """
    flag = 0
    stack = []
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == 0:
                continue
            else:
                if board[i][j].isalpha() and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    flag = 1
                    stack.append((i,j))
                    stack.append((i,j+1))
                    stack.append((i+1,j))
                    stack.append((i+1,j+1))
                else:
                    continue
    for coord in stack:
        y,x = coord
        board[y][x] = '*'
    add_ = len(set(stack))
    score += add_

    return score, board, flag

def pushing(m,n,board):
    new_board = []
    for _ in range(m):
        new_board.append([0]*n)
    
    for j in range(n):
        s = [board[i][j] for i in range(m)]
        while '*' in s:
            s.remove('*')
        s = list(map(str, s))

        s = ''.join(s).rjust(m, '#')
        s = list(s)
        for i in range(m):
            new_board[i][j] = s[i]
    
    return new_board

def solution(m, n, board):
    answer = 0
    # encode = {'R':1, 'M':2, 'A':3, 'F':4, 'N':5, 'T':6, 'J':7, 'C':8}
    new_board = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(board[i][j])
        new_board.append(temp)
    
    flag = 1
    while flag != 0:
        answer, new_board, flag = scoring(m, n, new_board, answer)
        # print(answer, new_board, '\n\n')
        new_board = pushing(m, n, new_board)
        # print(new_board)
        # break
    
    return answer

print(solution(4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]	))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))