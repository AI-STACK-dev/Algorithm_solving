import sys; input = sys.stdin.readline;
A, B = map(int, input().rstrip().split())
print((A + B) * (A - B))