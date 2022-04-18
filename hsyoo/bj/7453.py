import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
a_list, b_list, c_list, d_list = [],[],[],[]
for _ in range(n):
    a,b,c,d = map(int, input().split())
    a_list.append(a); b_list.append(b); c_list.append(c); d_list.append(d);


a_b, c_d = [],[]
for i in range(n):
    for j in range(n):
        a_b.append(a_list[i] + b_list[j])
        c_d.append(c_list[i] + d_list[j])

c = Counter(c_d)
ans = 0
for num in a_b:
    ans += c[-num]
print(ans)