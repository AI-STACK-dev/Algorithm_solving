import sys;input=sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().rstrip().split())))
    
data = sorted(data,key=lambda x: (x[1],x[0]))
for i in range(n):
    print(*data[i])