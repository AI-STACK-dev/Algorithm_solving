import sys; input = sys.stdin.readline;
K = int(input())
for i in range(K):
    C, B, n, r = map(int, input().split())
    R = r / 100
    BoC = set(list(map(int, input().split())))
    res = 0
    for _ in range(n):
        Ci, Pi = map(int, input().split())
        if Ci in BoC:
            res += int(Pi * R)
    print(f'Data Set {i + 1}:')
    print(res)
    print()