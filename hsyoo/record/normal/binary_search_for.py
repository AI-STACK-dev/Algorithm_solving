def binary_search(ary, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		if target == ary[mid]:
			return mid
		elif target < ary[mid]:
			end = mid - 1
		else:
			start = mid + 1
	return None
	

n, target = map(int, input().split())
ary = list(map(int, input().split()))

result = binary_search(ary, target, 0, n-1)
if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1)