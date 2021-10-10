def solution(s):
    ary = s
    result_ary = []
    length = len(s)
    for i in range(1,(length)//2+1):
        div = length//i
        cnt = 1
        unit_length = 0
        for j in range(1,div+1):
            pre = ary[i*(j-1):i*j]
            cur = ary[i*j:i*j+i]
            if pre == cur:
                cnt+=1
            else:
                if cnt!=1:
                    unit_length = unit_length + len(str(cnt))+i
                else:
                    unit_length += i
                cnt=1
        unit_length += len(cur)
        result_ary.append(unit_length)
    answer = min(result_ary)
    return answer