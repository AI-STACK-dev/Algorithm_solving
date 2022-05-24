"""from itertools import combinations 

def solution(relation):
    # answer = 0
    result = 0
    n = len(relation)
    m = len(relation[0])
    list_ = [i for i in range(m)]
    for comb_n in range(1, m+1):
        comb = list(combinations(list_, comb_n))
        print(f"comb : {comb}")
        for case in comb:
            print(f"case : {case}")
            dict_ = {}
            flag = 1
            for i in range(n):
                key_ = ''
                for j in case:
                    key_ += str(relation[i][j])

                if dict_.get(key_) == None:
                    dict_[key_] = 1
                else:
                    flag= 0
            if flag == 1:
                flag2 = 1
                if len(case) != 1:
                    temp = ''.join(case)
                    print(temp)
                result += 1
                for k in case:
                    if k in list_:
                        list_.remove(k)
                print(case)
                
    return result"""

from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])

    comb = []
    for i in range(1, m + 1):
        comb.extend(combinations(range(m), i))
    
    unique = []
    for i in comb:
        temp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(temp)) == n:
            flag = True

            for x in unique:
                print(x, i, set(x).issubset(set(i)))
                if set(x).issubset(set(i)):
                    flag = False
                    break
            if flag:
                unique.append(i)
    return len(unique)

# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation = [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]
# relation = [['100'], ['200'], ['100']]
print(solution(relation))