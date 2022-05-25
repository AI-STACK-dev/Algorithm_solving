from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque([])
    for progress, speed in zip(progresses, speeds):
        queue.append(math.ceil((100 - progress) / speed))
    
    base = queue.popleft()
    cnt = 1
    while queue:
        num = queue.popleft()
        if num <= base:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            base = num
    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]	))
print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]	))