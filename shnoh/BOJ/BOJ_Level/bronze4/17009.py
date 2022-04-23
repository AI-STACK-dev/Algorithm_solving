import sys; input = sys.stdin.readline;
A = [int(input()) for _ in range(3)]
B = [int(input()) for _ in range(3)]
Apoint = Bpoint = 0
for i in range(3):
    Apoint += A[i] * (3 - i)
    Bpoint += B[i] * (3 - i)
if Apoint > Bpoint:
    print('A')
elif Bpoint > Apoint:
    print('B')
else:
    print('T')