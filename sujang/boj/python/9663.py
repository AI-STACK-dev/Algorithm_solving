n = int(input())
ans = 0

def promising(idx):
    for i in range(idx):
        if board[idx] == board[i] or idx -i == abs(board[idx]-board[i]):
            return False
    return True

def nQueen(idx):
    global n, ans
    if idx == n:
        ans += 1
        return
    for i in range(n):
        board[idx] = i
        if promising(idx):
            nQueen(idx+1)


board = [0]*n
nQueen(0)
print(ans)