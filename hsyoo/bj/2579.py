import sys
n = int(input())
ary = [0] * 301
d = [0] * 301
for i in range(1,n+1):
    ary[i] = (int(sys.stdin.readline().rstrip()))

d[1] = ary[1]
d[2] = ary[1] + ary[2]
d[3] = max(ary[1] + ary[3], ary[2]+ary[3])
for i in range(4,n+1):
    d[i] = max(d[i-3] + ary[i-1] + ary[i], d[i-2] + ary[i])
print(d[n])