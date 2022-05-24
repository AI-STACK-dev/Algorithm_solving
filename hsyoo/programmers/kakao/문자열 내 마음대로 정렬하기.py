def solution(strings, n):
    answer = sorted(sorted(strings), key = lambda x : x[n])
    print(answer)
    return answer