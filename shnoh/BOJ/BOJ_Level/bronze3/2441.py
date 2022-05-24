import sys; input = sys.stdin.readline;
N = int(input())
stars = '*' * N
blank = ' ' * N
for i in range(N):
    temp = blank[:i] + stars[i:]
    print(temp)