import sys; input = sys.stdin.readline;
while True:
    N, D = map(int, input().split())
    if not N and not D:
        break
    check = [1] * N
    for _ in range(D):
        data = list(map(int, input().split()))
        for i in range(N):
            if not data[i]:
                check[i] = 0
    if sum(check):
        print("yes")
    else:
        print("no")