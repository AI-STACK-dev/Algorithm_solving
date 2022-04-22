from collections import Counter

def solution(numbers):
    answer = 0
    c = Counter(numbers)
    print(c)
    for num in range(1, 10):
        print(num, c[num])
        if c[num] == 0:
            answer += num
    print(answer)
    return answer