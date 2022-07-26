"""from itertools import combinations

n, m = map(int, input().split())
ary = list(map(int, input().split()))
comb = list(combinations(ary, 2))
answer= 0 
for case in comb:
    if case[0] == case[1]:
        continue
    answer +=1

print(answer)"""

# Solution time complexity O(n+m)
n,m = map(int, input().split())
ary = list(map(int, input().split()))
weight = [0] * 11
for case in ary:
    weight[case] +=1
answer = 0
for i in range(1, m+1):
    n -= weight[i]
    answer += weight[i] * n
print(answer)