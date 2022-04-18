n = int(input())
ary = list(map(int, input().split()))
ary.sort()

def two_pointer(ary, start, end):
    abs_min = int(1e10)
    while start < end:
        temp = ary[start] + ary[end]
        if abs(temp) < abs_min:
            al = start
            ar = end
            abs_min = abs(temp)
        if temp < 0:
            start += 1
        else:
            end -= 1
    return al, ar

start, end = two_pointer(ary, 0, n-1)
print(ary[start], ary[end])