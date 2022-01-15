import sys;input=sys.stdin.readline

n = int(input().rstrip())
data = [ list(map(int,input().rstrip().split())) for _ in range(n)]

ans = [0]*3

def recursion_find(x,y,n):
    val = data[x][y]
    flag = True
    # 전체 종이 확인
    for i in range(x,x+n):
        for j in range(y,y+n):
            if data[i][j] != val:
                flag = False
                break
    if flag:
        ans[val+1] += 1
        return
    
    # 9등분 하여 recursion
    n //=3
    recursion_find(x,y,n)
    recursion_find(x,y+n,n)
    recursion_find(x,y+(2*n),n)
    
    recursion_find(x+n,y,n)
    recursion_find(x+n,y+n,n)
    recursion_find(x+n,y+(2*n),n)
    
    recursion_find(x+(2*n),y,n)
    recursion_find(x+(2*n),y+n,n)
    recursion_find(x+(2*n),y+(2*n),n)

recursion_find(0,0,n)
print(*ans, sep='\n')