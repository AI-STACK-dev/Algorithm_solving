import sys; input = sys.stdin.readline;
import math
K = int(input())
for i in range(K):
    b, w = map(float, input().split())
    h = 0
    for _ in range(int(b)):
        r = float(input())
        h += r ** 3 * 4 * math.pi / 3
    print(f'Data Set {i + 1}:')
    if w * 1000 < h:
        print("Yes")
    else:
        print("No")
    print()