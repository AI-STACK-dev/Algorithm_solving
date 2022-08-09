import sys; input = sys.stdin.readline;
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    if a >= b:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")