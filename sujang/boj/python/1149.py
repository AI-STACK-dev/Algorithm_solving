import sys; input = sys.stdin.readline

n = int(input().rstrip())
data = [ list(map(int,input().rstrip().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(3):
        lst = [0,1,2]
        lst.remove(j)
        data[i][j] += min(data[i-1][lst[0]],data[i-1][lst[1]])
print(min(data[n-1]))