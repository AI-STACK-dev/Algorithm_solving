import sys; input = sys.stdin.readline;
M = int(input())
D = int(input())
res = M + D * 0.01
if res > 2.18:
    print("After")
elif res < 2.18:
    print("Before")
else:
    print("Special")