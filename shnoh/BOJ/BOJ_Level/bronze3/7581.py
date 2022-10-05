import sys; input = sys.stdin.readline;
while True:
    l, w, h, v = map(int, input().split())
    if not l and not w:
        break
    if not l:
        l = v // w // h
    if not w:
        w = v // l // h
    if not h:
        h = v // w // l
    if not v:
        v = l * w * h
    print(l, w, h, v)