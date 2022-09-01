import sys; input = sys.stdin.readline;
t = int(input())
data = [list(map(int, input().split())) for _ in range(t)]
for each in data:
    each = each[1:]
    odd = even = 0
    for k in each:
        if k % 2:
            odd += k
        else:
            even += k
    if odd > even:
        print("ODD")
    elif odd < even:
        print("EVEN")
    else:
        print("TIE")