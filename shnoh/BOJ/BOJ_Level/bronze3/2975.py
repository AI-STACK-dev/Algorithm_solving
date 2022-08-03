import sys; input = sys.stdin.readline;
while True:
    x, y, z = input().rstrip().split()
    b = int(x)
    a = int(z)
    if a or b:
        if y == 'W':
            c = b - a
            if c < -200:
                print("Not allowed")
            else:
                print(c)
        else:
            c = b + a
            print(c)
    else:
        break