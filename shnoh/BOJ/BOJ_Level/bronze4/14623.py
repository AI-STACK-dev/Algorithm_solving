import sys; input = sys.stdin.readline;
A = '0b' + input().rstrip()
B = '0b' + input().rstrip()
C = bin(int(A, 2) * int(B, 2))
C = C[2:]
print(C)