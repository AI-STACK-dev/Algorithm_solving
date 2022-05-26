import sys; input = sys.stdin.readline;
n, m = map(int, input().split())
Min = min(n, m)
Max = max(n, m)
res = (Min - 1) + Min * (Max - 1)
print(res)