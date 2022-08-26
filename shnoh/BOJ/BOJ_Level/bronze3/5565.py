import sys; input = sys.stdin.readline;
s = int(input())
data = [int(input()) for _ in range(9)]
print(s - sum(data))