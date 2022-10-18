import sys; input = sys.stdin.readline;
while True:
    try:
        x = input().rstrip()
        if x == "":
            break
        n, s = map(int, x.split())
        print(s // (n + 1))
    except EOFError:
        break