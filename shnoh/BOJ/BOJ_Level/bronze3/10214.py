import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    Y = K = 0
    for _ in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")