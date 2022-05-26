from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([])
    n = len(numbers)
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))
    while queue:
        # print(queue)
        num, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append((num+numbers[idx], idx))
            queue.append((num-numbers[idx], idx))
        else:
            if num == target:
                answer+=1
    return answer

print(solution([1, 1, 1, 1, 1]	, 3))