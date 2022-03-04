import sys; input = sys.stdin.readline;
T = int(input())
if T % 10 != 0:
    print(-1)
else:
    T = T // 10
    A = T // 30
    T = T % 30
    B = T // 6
    C = T % 6
    print(A, B, C)