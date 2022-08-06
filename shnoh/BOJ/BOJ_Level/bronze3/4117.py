import sys; input = sys.stdin.readline;
while True:
    n, t1, t2, t3 = map(int, input().split())
    if not n:
        break
    if t2 < t1:
        k1 = t2 - t1 + n
    else:
        k1 = t2 - t1
    if t2 < t3:
        k2 = t2 - t3 + n
    else:
        k2 = t2 - t3
    print(n * 4 - 1 + k1 + k2)