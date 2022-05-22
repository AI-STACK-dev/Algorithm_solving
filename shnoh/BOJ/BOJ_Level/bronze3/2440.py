import sys; input = sys.stdin.readline;
N = int(input())
stars = ['*'] * N
for i in range(N):
    print(*stars[i:], sep = '')