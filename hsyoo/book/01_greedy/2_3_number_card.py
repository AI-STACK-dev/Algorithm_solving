
n,m = map(int, input().split())
arr = list()
for _ in range(n):
    min_ = min(list(map(int, input().split())))
    arr.append(min_)
print(max(arr))
