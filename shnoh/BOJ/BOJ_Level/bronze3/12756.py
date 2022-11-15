import sys; input = sys.stdin.readline;
import math
aa, al = map(int, input().split())
ba, bl = map(int, input().split())

at = math.ceil(al / ba)
bt = math.ceil(bl / aa)
if at > bt:
    print("PLAYER A")
elif at < bt:
    print("PLAYER B")
else:
    print("DRAW")