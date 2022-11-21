from collections import deque

def solution(queue1, queue2):
    answer = 0
    limit = len(queue1) * 3
    sum1, sum2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    
    for i in range(limit):
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
            answer += 1

        else:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
            answer += 1
    return -1

print(solution([3, 2, 7, 2]	, [4, 6, 5, 1]	))
print(solution([1, 2, 1, 2]	, [1, 10, 1, 2]	))
print(solution([1,1]	, [1,5]	))
