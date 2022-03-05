import sys; input = sys.stdin.readline;
A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P
if P > C:
    Y = B + (P - C) * D
else:
    Y = B

print(min(X, Y))