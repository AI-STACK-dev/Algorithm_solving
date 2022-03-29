import sys; input = sys.stdin.readline;
Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

B = max(abs(Br - Jr),abs(Bc - Jc))
D = abs(Jr - Dr) + abs(Jc - Dc)
if B > D:
    print("daisy")
elif B < D:
    print("bessie")
else:
    print("tie")