import sys; input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(2)]
    for i in range(1,n):
        if i == 1:
            data[0][i] += data[1][i-1]
            data[1][i] += data[0][i-1]
        else:
            data[0][i] += max(data[1][i-1],data[1][i-2])
            data[1][i] += max(data[0][i-1],data[0][i-2])         
    print(max(data[0][-1], data[1][-1]))
    