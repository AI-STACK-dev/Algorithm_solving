import heapq

## 최소 힙 생성
"""
heapq 모듈에는 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와준다!
그렇기 때문에, 그냥 빈 리스트를 생성해놓은 다음 heapq 모듈의 함수를 호출할 때 마다 이 리스트를 인자로 넘긴다.
다시 말해, 파이썬에서는 heapq 모듈을 통해서 원소를 추가하거나 삭제한 리스트가 그냥 최소힙!!!!
"""

heap = []

## 힙에 원소 추가
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

## 힙에서 원소 삭제
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)

## 기존 리스트를 힙으로 변환
heap = [4,1,7,3,8,5]
heapq.heapify(heap)
print(heap)

## [응용] 최대 힙
"""
heapq는 최소 힙을 기능만으로 동작하기 때문에 최대(max heap)으로 하려면 요령이 필요.
힙에 튜플을 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로
최소힙이 구성되는 원리 이용
"""

nums = [4,1,7,3,8,5]
heap = []
for num in nums:
    heapq.heappush(heap, (-num, num))
while heap:
    print(heapq.heappop(heap)[1])

## [응용] k번째 최소값 / 최대값
def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(heap)
    return kth_min
print(kth_smallest([4,1,7,3,8,5], 3))

## [응용] 힙 정렬
def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums
print(heap_sort([4,1,7,3,8,5]))