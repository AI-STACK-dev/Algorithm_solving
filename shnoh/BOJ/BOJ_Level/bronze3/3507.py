import sys; input = sys.stdin.readline;
n = int(input())
k = min(abs(n - 99), 100)
print(100 - k)