# 바구니에 쌓인다. -> stack /// stack에 넣었을 때, stack[-1]과 같은 숫자일 경우, stack pop & answer += 2
# move의 원소는 배열의 크기만큼임!! 
# 우선 move를 받았을 때, 맨 위에 있는 원소를 체크해야함. -> 0이 아닌 다른 숫자 중 제일 앞에. (flag를 설정해서 찾으면 True)
# 해당 index를 받고, 그 해당 인덱스의 숫자를 stack에 넣은 후, 해당 index는 0로 replace
# 그 후 해당 리스트를 원래의 board에 다시 replace 해준다.

def pick(board, move_idx):
    n = len(board)
    # print(n)
    n_board = board.copy()
    # temp = []
    # for i in range(n):
    #     temp.append(n_board[i][move_idx])
    temp = [n_board[x][move_idx] for x in range(n)]

    pick_idx = -1
    for i in range(n):
        if temp[i] != 0:
            pick_idx = i
            num = temp[i]
            temp[i] = 0
            break

    if pick_idx == -1:
        return n_board, -1
    for i in range(n):
        n_board[i][move_idx] = temp[i]
    return board, num

def solution(board, moves):
    answer= 0 
    stack = []
    for move in moves:
        move_idx = move - 1
        board, num = pick(board, move_idx)
        if num == -1:
            continue
        else:
            if len(stack) == 0:
                stack.append(num)
            elif len(stack) > 0 and stack[-1] == num:
                stack.pop()
                answer += 2
            elif len(stack) > 0 and stack[-1] != num:
                stack.append(num)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))