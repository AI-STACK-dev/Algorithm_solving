n = int(input())
data = [ list(map(int,input().split())) for _ in range(n)]
data = sorted(data,key=lambda x : (x[0],x[1]))
for i in range(n):
    print(*data[i])