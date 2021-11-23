import heapq as hp

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    data = []
    for i,f in enumerate(food_times):
        hp.heappush(data,[f,i+1])
        
    sub = 0
    n = len(food_times)
    for _ in range(n):
        time = (data[0][0]-sub)*n
        if time > k:
            a = [d[1] for d in data]
            a.sort()
            return a[k%n]
        else:
            d = hp.heappop(data)
            k -= time
            sub = d[0]
            n -= 1