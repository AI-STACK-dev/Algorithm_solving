import sys; input = sys.stdin.readline;
s = input().rstrip()
cnt = 0
setA = {'a','e','i','o','u'}
for c in s:
    if c in setA:
        cnt += 1
print(cnt)