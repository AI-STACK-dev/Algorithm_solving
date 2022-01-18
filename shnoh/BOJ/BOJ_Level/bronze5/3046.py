import sys; input = sys.stdin.readline;
R1, S = map(int, input().split())
# (r1 + r2) / 2 = s
# 2s - r1 = r2
print(2 * S - R1)