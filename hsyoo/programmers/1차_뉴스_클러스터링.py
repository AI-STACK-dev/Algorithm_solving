from collections import Counter
from copy import deepcopy

def make_set(str_):
    list_ = []
    str_ = str_.lower()
    for i in range(len(str_) - 1):
        if str_[i].isalpha() and str_[i+1].isalpha():
            list_.append(str_[i:i+2])
    return list_
def solution(str1, str2):
    list_a = make_set(str1)
    list_b = make_set(str2)
    if len(list_a) == 0 and len(list_b) == 0:
        return 1*65536
    else:
        list_union = deepcopy(list_a)
        c1 = Counter(list_a)
        print(c1.keys())
        print(list(c1.elements()))
        for case in list_b:
            if c1[case] == 0:
                list_union.append(case)
            else:
                c1[case] -= 1
        
        list_inter = []
        c2 = Counter(list_a)
        for case in list_b:
            if c2[case] >=1:
                list_inter.append(case)
                c2[case] -= 1
        return int(len(list_inter) / len(list_union) * 65536)

# print(solution([1,1,2,2,3], [1,2,2,4,5]))
print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

    
