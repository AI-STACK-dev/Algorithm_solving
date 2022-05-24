from collections import Counter

def solution(lottos, win_nums):
    c = Counter(lottos)
    zeros = c[0]
    dict_ = {'6':1, '5':2, '4' : 3, '3':4, '2' : 5, '1' : 6, '0' : 6}
    result = 0
    for case in win_nums:
        if case in lottos:
            result +=1
    
    # if zeros == 0:
    #     return [dict_[str(result)], dict_[str(result)]]
    # else:
    return [dict_[str(result + zeros)], dict_[str(result)]]