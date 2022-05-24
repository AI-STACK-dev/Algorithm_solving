from collections import Counter

def solution(s):
    answer = []
    str_ = ''
    ary = []
    for case in s:
        if case.isdigit():
            str_ += case
        else:
            if len(str_) > 0:
                ary.append(int(str_))
                str_ = ''
            else:
                continue
    c = Counter(ary)
    answer = [i[0] for i in c.most_common()]
    # print(c.most_common())
    return answer