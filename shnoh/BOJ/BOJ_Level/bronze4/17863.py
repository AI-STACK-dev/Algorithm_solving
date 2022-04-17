import sys; input = sys.stdin.readline;
N = input().rstrip()
prefix = N[:3]
if prefix == "555":
    print("YES")
else:
    print("NO")