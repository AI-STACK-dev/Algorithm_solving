import sys; input = sys.stdin.readline;
a, b, c = map(int, input().split())
print(max(b - a, c - b) - 1)