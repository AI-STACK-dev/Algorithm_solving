from itertools import combinations
n, m = map(int, input().split())
values=list(map(int, input().split()))
idx_ary = [x for x in range(n)]
cnt = 0 
comb = list(combinations(idx_ary, 2))

for idx0, idx1 in comb:
    if values[idx0] == values[idx1]:
        continue
    else:
        cnt +=1
print(cnt)