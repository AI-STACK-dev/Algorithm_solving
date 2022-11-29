import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    n = int(input())
    C = G = 0
    for _ in range(n):
        a, b = input().split()
        c = int(a)
        g = float(b)
        C += c
        G += c * g
    print(f"{C} {G/C:.1f}")