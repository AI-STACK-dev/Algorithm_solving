import sys; input = sys.stdin.readline;
import math
n = int(input())
cnt = 0
for x in range(1, math.ceil(n ** 0.5)):
    if n % x == 0:
        y = n // x
        if (x + y) % 2 == 0:
            cnt += 1
            # a = (x + y) / 2
            # b = (y - x) / 2 
print(cnt)