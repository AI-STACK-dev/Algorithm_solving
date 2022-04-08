import heapq as hp

def solution(s, k):
    ans = 0
    s.sort()
    while True:
        first = hp.heappop(s)
        if first >= k:
            return ans
        elif len(s) == 0:
            return -1
        second = hp.heappop(s)
        hp.heappush(s, first + (second*2))
        ans += 1
