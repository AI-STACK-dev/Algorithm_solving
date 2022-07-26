import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    a,b = input().rstrip().split()
    if b == "kg":
        print(f'{float(a) * 2.2046 :.4f} lb')
    elif b == "lb":
        print(f'{float(a) * 0.4536 :.4f} kg')
    elif b == "l":
        print(f'{float(a) * 0.2642 :.4f} g')
    elif b == "g":
        print(f'{float(a) * 3.7854 :.4f} l')