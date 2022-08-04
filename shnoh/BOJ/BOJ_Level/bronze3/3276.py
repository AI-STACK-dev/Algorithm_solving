import sys; input = sys.stdin.readline;
import math
n = int(input())
k = math.ceil(n ** 0.5)
if n <= k * (k - 1):
    print(k, k - 1)
else:
    print(k, k)