n = int(input())
cnt = 1
param = 1
while n > param:
    param += 6*cnt
    cnt += 1
print(cnt)