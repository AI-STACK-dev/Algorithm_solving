import heapq

def solution(scovilles, K):
    answer = 0
    q = []
    for scoville in scovilles:
        heapq.heappush(q, scoville)
    while q:
        num = heapq.heappop(q)
        if num >= K:
            return answer
        else:
            if len(q) >= 1:
                temp = heapq.heappop(q)
                num += (temp*2)
                answer += 1
                heapq.heappush(q, num)
            else:
                return -1

    # return answer

print(solution([1, 2, 3, 9, 10, 12]	, 7))