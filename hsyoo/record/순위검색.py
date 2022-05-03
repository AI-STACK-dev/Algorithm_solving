from itertools import combinations
from bisect import bisect_left
import copy
def solution(information, queries):
    dict_ = {}
    for info in information:
        temp = info.split(' ')
        data = temp[:-1]
        value_ = int(temp[-1])
        for i in range(5):
            comb = combinations([0,1,2,3], i)
            for k in list(comb):
                data_temp = copy.copy(data)
                for v in k:
                    data_temp[v] = '-'
                key_ = '_'.join(data_temp)
                if dict_.get(key_) == None:
                    dict_[key_] = [value_]
                else:
                    dict_[key_].append(value_)
    for value in dict_.values():
        value.sort()
    
    answer = []
    for query in queries:
        query = query.replace(' and', ' ')
        query = query.split()
        key_ = '_'.join(query[:-1])
        score = int(query[-1])
        if dict_.get(key_) != None:
            answer.append(len(dict_[key_]) - bisect_left(dict_[key_], score))
        else:
            answer.append(0)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# info = ["java backend junior pizza 150"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# query = ["- and - and - and - 150"]
print(solution(info, query))