import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    d, n, s, p = map(int, input().split())
    S = n * s
    P = n * p + d
    if S > P:
        print("parallelize")
    elif S < P:
        print("do not parallelize")
    else:
        print("does not matter")