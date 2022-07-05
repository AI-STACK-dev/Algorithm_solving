def solution(n, fears):
    answer = 0
    fears.sort(reverse = True)
    idx = 0

    while True:
        if idx < n and idx + fears[idx] <= n:
            answer += 1
            idx += fears[idx]
        else:
            break 
    return answer

n = int(input())
fears = list(map(int, input().split()))
print(solution(n, fears))