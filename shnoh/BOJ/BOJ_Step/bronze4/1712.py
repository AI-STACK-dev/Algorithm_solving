import sys; input = sys.stdin.readline;
N = 2100000000
A, B, C = map(int, input().split())
def solve(A, B, C):
    if B >= C:
        return -1
    else:
        return A // (C - B) + 1
print(solve(A, B, C))
