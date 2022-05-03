from collections import defaultdict

def solution(fees, records):
    dict_ = defaultdict(list)
    dict_val = defaultdict(int)
    for record in records:
        time, car_num, cmd = record.split(' ')
        h, m = time.split(':')
        h_ = 60*int(h)
        m = int(m) + h_ 
        dict_[car_num].append(m)
    for key_ in dict_.keys():
        if len(dict_[key_]) % 2 != 0:
            dict_[key_].append(1439)
    
    ans = []
    for key_ in dict_.keys():
        res = 0
        for i in range(0, len(dict_[key_]), 2):
            res += (dict_[key_][i+1] - dict_[key_][i])
        dict_val[key_] = res
        if res <= fees[0]:
            ans.append((int(key_), fees[1]))
        else:
            div = (res - fees[0]) // fees[2]
            residue = (res - fees[0]) % fees[2]
            if residue != 0:
                div +=1
            value = fees[1] + div * fees[3]
            ans.append((int(key_), value))
    ans.sort()
    answer = [i[1] for i in ans]

    # answer = []
    return answer

# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
fees = [1, 461, 1, 10]
records = 	["00:00 1234 IN"]
print(solution(fees, records))