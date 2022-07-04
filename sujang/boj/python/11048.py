import sys; input = sys.stdin.readline

n,m = map(int,input().split())
field = [ [0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j in range(1,m+1):
        field[i][j] = temp[j-1] + max(field[i][j-1], field[i-1][j], field[i-1][j-1])

print(field[n][m])
