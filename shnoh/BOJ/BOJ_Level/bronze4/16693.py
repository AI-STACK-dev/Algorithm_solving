import sys; input = sys.stdin.readline;
import math
a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

Slice = p1 / a1
Whole = p2 / (r1 ** 2 * math.pi)

if Slice > Whole:
    print("Whole pizza")
else:
    print("Slice of pizza")