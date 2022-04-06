import sys; input = sys.stdin.readline;
N, M = map(int, input().split())
res = min(N, M) // 2
print(res)