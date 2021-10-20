from sys import stdin

input = stdin.readline
r,c = map(int,input().rstrip().split())
data = [ list(map(lambda x: ord(x)-65,input().rstrip())) for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer =1
def dfs(x,y,ans):
    global answer

    answer = max(ans,answer)
    
    for i in range(4):
        X,Y = x+dx[i],y+dy[i]
        if 0<=X<r and 0<=Y<c and alp[data[X][Y]]==0:
            alp[data[X][Y]]=1
            dfs(X,Y,ans+1)
            alp[data[X][Y]]=0

alp = [0 for _ in range(26)]
alp[data[0][0]]=1
dfs(0,0,answer)
print(answer)
