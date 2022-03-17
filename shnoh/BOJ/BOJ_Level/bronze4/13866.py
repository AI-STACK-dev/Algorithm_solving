import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
A = max(data) + min(data)
B = sum(data) - A
print(abs(A - B))