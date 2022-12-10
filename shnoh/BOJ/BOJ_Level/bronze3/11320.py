import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print((a // b) ** 2)