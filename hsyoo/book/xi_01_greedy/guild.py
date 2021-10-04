n = int(input())
ary = list(map(int, input().split()))
ary.sort()
start, end = 0, 1
cnt = 0
while True:
    if end > n:
        break
    req = max(ary[start:end])
    if req > (end - start):
        end += 1
    else:
        cnt+=1
        start = end
        end += 1
    print(start, end)
print(cnt)