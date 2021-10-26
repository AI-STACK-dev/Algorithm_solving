from sys import stdin

n = int(stdin.readline().rstrip())
data = list(map(int,stdin.readline().rstrip().split()))

data.sort()

if len(data)%2==0:
    print(data[(len(data)//2) -1])
else:
    print(data[len(data)//2])