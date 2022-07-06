from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

right = bisect_right(arr, x)
left = bisect_left(arr, x)

if right - left == 0:
    print(-1)
else:
    print(right - left)