import sys; input = sys.stdin.readline;
D, H, M = map(int, input().split())
H += D * 24
M += H * 60
Eleven = 60 * (11 + 11 * 24) + 11

if Eleven > M:
    print(-1)
else:
    print(M - Eleven)