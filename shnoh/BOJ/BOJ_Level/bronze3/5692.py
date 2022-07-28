import sys; input = sys.stdin.readline;
import math
while True:
    n = input().rstrip()
    res = 0
    if n == '0':
        break
    for i in range(len(n)):
        res += math.factorial(i + 1) * int(n[- i - 1])
    print(res)