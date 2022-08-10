import sys; input = sys.stdin.readline;
while True:
    a,b,c,d = map(int, input().split())
    if a == 0:
        break
    A = max(a,b)
    B = min(a,b)
    C = max(c,d)
    D = min(c,d)
    res = max(min(int(min(C / A, D / B) * 100), 100), 1)
    print(f'{res}%')