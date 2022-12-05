import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    u = 2 * m - n
    print(u, m - u)