import sys; input = sys.stdin.readline;
ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
bx = cx - az
by = cy // ay
bz = cz - ax
print(bx, by, bz)