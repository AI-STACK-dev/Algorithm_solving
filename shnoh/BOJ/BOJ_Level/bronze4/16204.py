import sys; input = sys.stdin.readline;
N, M, K = map(int, input().split())
O = min(K, M)
X = min(N - M, N - K)
print(O + X)