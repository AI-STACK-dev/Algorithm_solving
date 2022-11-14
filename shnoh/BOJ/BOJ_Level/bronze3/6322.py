import sys; input = sys.stdin.readline;
cnt = 1
while True:
    a, b, c = map(int, input().split())
    if not a: break
    print(f"Triangle #{cnt}")
    if c != -1 and (a >= c or b >= c):
        print("Impossible.")
    else:
        if c == -1:
            x = (a ** 2 + b ** 2) ** 0.5
            print(f"c = {x:.3f}")
        elif b == -1:
            x = (c ** 2 - a ** 2) ** 0.5
            print(f"b = {x:.3f}")
        else:
            x = (c ** 2 - b ** 2) ** 0.5
            print(f"a = {x:.3f}")
    print()
    cnt += 1