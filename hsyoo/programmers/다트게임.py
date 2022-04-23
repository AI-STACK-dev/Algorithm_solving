def solution(dartResult):
    sum_ = 0
    pointer = 0
    num_ary = []
    check_pt = 0 
    n = len(dartResult)
    cmd = ['S', 'D', 'T']
    while pointer < n:
        if dartResult[pointer].isdigit():
            if dartResult[pointer+1].isdigit():
                # 10 check
                if len(dartResult[pointer:]) > 2 and dartResult[pointer+1].isdigit:
                    temp = int(dartResult[pointer : pointer + 2])
                    pointer += 2
            else:
                """
                0 ~ 9
                """
                temp = int(dartResult[pointer])
                pointer += 1
        if dartResult[pointer] in cmd:
            if dartResult[pointer] == 'D':
                temp = temp ** 2
            elif dartResult[pointer] == 'T':
                temp = temp ** 3
            pointer += 1
        if pointer < n and dartResult[pointer] in ['*', '#']:
            if dartResult[pointer] == '*':
                if len(num_ary) > 0:
                    num_ary[-1] = num_ary[-1] * 2
                temp = temp * 2
                pointer += 1
            else:
                temp = temp * (-1)
                pointer += 1
        num_ary.append(temp)
        check_pt += 1
    return sum(num_ary)