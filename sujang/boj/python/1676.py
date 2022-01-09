import sys;input= sys.stdin.readline

n = int(input())
ans = 0
while n>=5:
    n //=5
    ans += n
print(ans)