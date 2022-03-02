import sys; input = sys.stdin.readline;
C, D = map(int, input().split())
A = (C + D) // 2
B = (C - D) // 2
if (C + D) % 2 or (C - D) % 2 or A < 0 or B < 0:
    print(-1)
else:
    print(A, B)
