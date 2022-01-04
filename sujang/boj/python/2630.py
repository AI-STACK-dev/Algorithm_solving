import sys; input = sys.stdin.readline

n = int(input())
data = [ list(map(int,input().rstrip().split())) for _ in range(n)]

ans = [0,0]

def check_color(n,x,y):
    white = 0
    blue = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if data[i][j] == 0:
                white += 1
            else:
                blue += 1
    if white == (n**2):
        return 0
    elif blue == (n**2):
        return 1
    else:
        return -1

def split_paper(n,x,y):
    
    # n 크기의 색종이 확인
    result = check_color(n,x,y)
    if result != -1:
        ans[result] += 1
        return

    # n//2 크기의 색종이 확인
    for i in range(2):
        for j in range(2):   
                split_paper(n//2,x+((n//2)*i),y+((n//2)*j))
    return

split_paper(n,0,0)
print(*ans,sep ='\n')