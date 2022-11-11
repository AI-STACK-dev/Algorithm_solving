import sys; input = sys.stdin.readline;
t = int(input())
data = [[int(input()), i] for i in range(1, t + 1)]
data.sort()
for x in data:
    print(x[1])