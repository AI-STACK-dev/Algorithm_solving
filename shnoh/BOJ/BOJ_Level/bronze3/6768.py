import sys; input = sys.stdin.readline;
import math
J = int(input())
if J < 4:
    print(0)
else:
    print(math.factorial(J - 1) // math.factorial(3) // math.factorial(J - 4))