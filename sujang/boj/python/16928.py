import sys; input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
board = [0]*101
visisted = [int(1e9)]*101

# ladder & snake
for _ in range(n+m):
    a,b = map(int,input().rstrip().split())
    board[a] = b

ans = int(1e9)

def dfs(idx, cnt):
    global ans
    if idx == 100:
        ans = min(ans,cnt)
        return
    
    # ladder or snake
    if board[idx] > 0:
        dfs(board[idx],cnt)
        return

    visisted[idx] = min(cnt,visisted[idx])
    
    # check all
    for i in range(1,7):
        if idx+i <= 100 and cnt +1 < visisted[idx+i]:
            visisted[idx+i] = cnt + 1
            dfs(idx+i,cnt+1)
            
dfs(1,0)
print(ans)