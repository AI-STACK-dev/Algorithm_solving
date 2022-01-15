import sys; input = sys.stdin.readline;
L, P = map(int, input().split())
data = list(map(int, input().split()))
NP = L * P
for i in range(5):
    data[i] -= NP
print(*data)