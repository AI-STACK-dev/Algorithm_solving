n = int(input())
ary = list(map(int, input().split()))
total = int(input())

def binary_search(ary, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum_temp = 0
        for case in ary:
            if case <= mid :
                sum_temp += case
            else:
                sum_temp += mid
        if sum_temp <= total:
            am = mid
            start = mid + 1

        else:
            end = mid - 1
    return am

sum_ = sum(ary)
max_ = max(ary)
min_ = min(ary)
# ary.sort()
if sum_ <= total:
    print(max_)
else:
    print(binary_search(ary, 1, total))