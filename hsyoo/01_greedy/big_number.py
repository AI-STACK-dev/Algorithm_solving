n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)
cnt = 0
sum = 0
for i in range(m):
    cnt +=1
    if cnt <= k:
        sum += arr[0]
    else:
        sum += arr[1]
        cnt = 0
print(sum)
