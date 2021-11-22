import sys; input = sys.stdin.readline

n = 1000 - int(input().rstrip())
d = [500,100,50,10,5,1]
cnt = 0

for dd in d:
    cnt += (n//dd)
    n %= dd
print(cnt)