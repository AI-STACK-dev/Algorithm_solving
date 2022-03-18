import sys; input = sys.stdin.readline;
data = list(input().rstrip().split())
if int(data[0]) + int(data[2]) == int(data[4]):
    print("YES")
else:
    print("NO")