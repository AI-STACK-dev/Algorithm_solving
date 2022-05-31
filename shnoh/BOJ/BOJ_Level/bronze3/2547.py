import sys; input = sys.stdin.readline;
T = int(input())
for i in range(T):
    input()
    N = int(input())
    data = [int(input()) for _ in range(N)]
    if sum(data) % N:
        print("NO")
    else:
        print("YES")