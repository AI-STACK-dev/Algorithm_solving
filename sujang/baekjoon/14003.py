from sys import stdin
from bisect import bisect_left as BL

n = int(stdin.readline())
data = list(map(int,stdin.readline().split()))

d = []
data_ = []

for a in data:
    if not d or a > d[-1]:
        d.append(a)
        data_.append((len(d)-1,a))
    else:
        idx = BL(d,a)
        d[idx] = a
        data_.append((idx,a))

ans = [0]*len(d)
li = len(d)-1
for i in range(n-1,-1,-1):
    if data_[i][0] == li:
        ans[li] = data_[i][1]
        li-=1
print(len(ans))
print(*ans)
