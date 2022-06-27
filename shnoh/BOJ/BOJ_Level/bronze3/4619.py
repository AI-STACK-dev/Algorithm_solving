import sys; input = sys.stdin.readline;
import math
while True:
    b,n = map(int, input().split())
    if not b and not n: break
    a = b ** (1/n)
    floor = math.floor(a)
    ceil = math.ceil(a)
    if abs(floor ** n - b) < abs(ceil ** n - b):
        print(floor)
    else:
        print(ceil)