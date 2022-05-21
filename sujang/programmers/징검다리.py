def check_possible(stones,k,x):
    prev = 0
    for s in stones:
        # 밟을 수 있는 돌
        if s >= x:
            if prev >= k:
                return False
            prev = 0
        else:
            prev += 1
    # exit condition
    if prev >= k:
        return False
    return True
            
def binary_search(stones,k):
    lo,hi = 1,200000000
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check_possible(stones,k,mid):
            lo = mid
        else:
            hi = mid
    return lo
def solution(stones, k):
    return binary_search(stones,k)
