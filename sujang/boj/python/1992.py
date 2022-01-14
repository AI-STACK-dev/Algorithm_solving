import sys;input = sys.stdin.readline

n = int(input())
data = [list(map(int,list(input().rstrip())))  for _ in range(n)]
ans = ""

def recursiveFunc(leftx,lefty,n):
    global ans
    
    # 전체 check 
    val = data[leftx][lefty]    
    for i in range(leftx, leftx+n):
        for j in range(lefty,lefty+n):
            if val != data[i][j]:
                val = -1
                break
            
    if val != -1:
        ans += str(val)
        return 
    
    # 4개로 나누기
    n //= 2
    ans += "("
    recursiveFunc(leftx,lefty,n)
    recursiveFunc(leftx,lefty+n,n)
    recursiveFunc(leftx+n,lefty,n)
    recursiveFunc(leftx+n,lefty+n,n)
    ans += ")"

recursiveFunc(0,0,n)
print(ans)