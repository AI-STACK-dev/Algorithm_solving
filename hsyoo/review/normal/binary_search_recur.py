def binary_search(ary, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return None
    if target == ary[mid]:
        return mid
    elif target < ary[mid]:
        return binary_search(ary, target, start, mid - 1)
    else:
        return binary_search(ary, target, mid + 1, end)
	


n, target = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()

result = binary_search(ary, target, 0, n-1)
if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1)