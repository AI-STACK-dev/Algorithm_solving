import sys; input = sys.stdin.readline;
A, B = map(int, input().rstrip().split())
C, D = map(int, input().rstrip().split())
print(min(A + D, B + C))