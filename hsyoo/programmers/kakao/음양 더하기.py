def solution(absolutes, signs):
    answer = 0
    for idx, num in enumerate(absolutes):
        if signs[idx] == True:
            answer += num
        else:
            answer -= num
        print(answer)
    return answer