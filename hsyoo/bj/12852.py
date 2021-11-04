import sys
import time
stime = time.time()
n = int(sys.stdin.readline().rstrip())
d = [(0, 1)] * (n+1)

for i in range(2,n+1):
    d[i] = (d[i-1][0] + 1, i-1)
    if i % 2 == 0:
        d[i] = min(d[i], (d[i//2][0] + 1, i//2))
    if i % 3 == 0:
        d[i] = min(d[i], (d[i//3][0] + 1, i//3))
print(d[n][0])
temp = d[n]
print(n, end = ' ')
while temp[1] != 1 :
    print(temp[1], end = ' ')
    temp = d[temp[1]]
if n != 1:
    print(1, end = ' ')
