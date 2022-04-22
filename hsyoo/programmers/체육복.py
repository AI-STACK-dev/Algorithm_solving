def solution(n, lost, reserve):
    # for num in lost:
    #     if num in reserve:
    #         lost.remove(num)
    #         reserve.remove(num)
    #     print(lost, reserve)
    # print(lost, reserve)
    lost_ = [i for i in lost if i not in reserve]
    reserve_ = [i for i in reserve if i not in lost]
    # print(lost_, reserve_)
    ary = [False] * (n+1)
    for num in reserve_:
        ary[num] = True
    cnt = 0
    for num in set(lost_):
        if num-1>=0 and ary[num-1] == True:
            ary[num-1] = False
        elif num+1<=n and ary[num+1] == True:
            ary[num+1] = False
        else:
            cnt += 1
            
    answer = n - cnt
    print(answer)
    return answer