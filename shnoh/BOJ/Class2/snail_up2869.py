import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
# cur = 0
# day = 0
# while True:
#     day += 1
#     cur += a
#     if cur >= v: break
#     else: cur -= b
v= v - a
step = a- b
print(math.ceil(v / step) + 1)