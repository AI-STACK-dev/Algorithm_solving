import sys; input = sys.stdin.readline;
A, B, C = map(int, input().split())
D = int(input())
C += D
B += C // 60
C = C % 60
A += B // 60
B = B % 60
A = A % 24
print(A, B, C)