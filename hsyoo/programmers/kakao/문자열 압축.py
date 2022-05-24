def solution(s):
    result = []
    for step in range(1, len(s)+1):
        print(step)
        temp = ''
        pre = ''
        s_ans = ''
        cnt = 1
        for case in s:
            if len(temp) < step:
                temp += case
            elif len(temp) == step and len(pre) == 0:
                pre = temp
                temp = ''
            elif len(temp) == step and len(pre) != 0:
                if pre == temp:
                    cnt += 1
                else:
                    s_ans += str(cnt)
                    s_ans += temp
                    pre = temp
                    cnt = 1
                temp = ''
            else:
                print("WOWOWOWO")
        s_ans += temp
        result.append(s_ans)
    print(result)
    return result
                    
print(solution("aabbaccc"))