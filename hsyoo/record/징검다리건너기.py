def solutions(stones, k):
    left = 1 
    right = int(2e8)
    while left <= right:
        mid = (left + right) // 2
        temp = stones.copy()
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left
