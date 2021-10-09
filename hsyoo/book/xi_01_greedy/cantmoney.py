from itertools import combinations
n = int(input())
ary = list(map(int, input().split()))
sum_ary = []
for i in range(n):
    sum_ary.extend(list(map(sum, list(combinations(ary, i)))))
cnt = 1
while True:
    if cnt not in sum_ary:
        break
    else:
        cnt+=1
print(cnt)