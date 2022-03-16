import math
import sys; input = sys.stdin.readline;
R, C, N = map(int, input().split())
x = math.ceil(R / N)
y = math.ceil(C / N)
print(x * y)