import sys; input = sys.stdin.readline;
S, T, D = map(int, input().split())
res = D / (S * 2)
print(int(res * T ))