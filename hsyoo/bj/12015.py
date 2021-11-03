import sys
n = int(input())
ary = list(map(int, sys.stdin.readline().rstrip().split()))
ary.sort()
result = 1
for i in range(1,n):
    pre = ary[i-1]
    cur = ary[i]
    if pre < cur:
        result+=1
print(result)