import sys; input = sys.stdin.readline;
A, B = map(int, input().split())
q = A // B
r = A % B
if r < 0:
    q += 1
    r += abs(B)
print(q)
print(r)