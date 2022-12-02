import sys; input = sys.stdin.readline;
while True:
    l, w, a = map(int, input().split())
    if not l and not w:
        break
    if not a:
        a = l * w
    elif not l:
        l = a // w
    else:
        w = a // l
    print(l, w, a)