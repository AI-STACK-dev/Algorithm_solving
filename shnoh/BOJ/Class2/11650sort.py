import sys; input = sys.stdin.readline;

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()
for i in range(n):
    print(data[i][0], data[i][1])