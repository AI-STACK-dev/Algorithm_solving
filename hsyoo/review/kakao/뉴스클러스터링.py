from collections import Counter

def get_list(s):
    n = len(s)
    list_ = []
    for i in range(n-1):
        if s[i].isalpha() and s[i+1].isalpha():
            list_.append(s[i]+s[i+1])
    return list_

def similarity(s1, s2):
    inter_ = set(s1) & set(s2)
    inter_ = list(inter_)
    a = Counter(s1)
    b = Counter(s2)
    inter_value = 0
    for case in inter_:
        inter_value += min(a[case], b[case])
    a.update(b)
    union_value = sum(a.values()) - inter_value
    return inter_value / union_value

def solution(str1, str2):
    str1 = str1.lower()
    str2  = str2.lower()
    str1, str2 = get_list(str1), get_list(str2)
    if len(str1) == 0 and len(str2) == 0:
        return 65536
    sim = similarity(str1, str2)
    return int(sim * 65536)

print(solution('FRANCE', 'french'))
print(solution("handshake", 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))