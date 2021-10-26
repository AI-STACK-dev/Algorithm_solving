from sys import stdin

n = int(stdin.readline().rstrip())
data = [list(stdin.readline().rstrip().split()) for _ in range(n)]

data.sort(key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for d in data:
    print(d[0])
