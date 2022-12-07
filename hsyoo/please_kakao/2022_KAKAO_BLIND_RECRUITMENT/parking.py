from collections import defaultdict
import math

def hour2int(hour):
    h, m = map(int, hour.split(':'))
    h *= 60
    result = h+m
    return result


def solution(fees, records):
    answer = []
    log = defaultdict(list)
    total_sum = defaultdict(int)
    for record in records:
        hour, car_num, _ = record.split()
        hour = hour2int(hour)
        log[car_num].append(hour)

        
    for car_num in log.keys():
        length = len(log[car_num])
        if length % 2 != 0:
            log[car_num].append(hour2int("23:59"))
        for i in range(0, length, 2):
            # print(car_num, i, log[car_num])
            total_sum[car_num] += (log[car_num][i+1] - log[car_num][i])
    
    for car_num in sorted(log.keys()):
        if total_sum[car_num] <= fees[0]:
            answer.append(fees[1])
        else:
            result = fees[1] + math.ceil((total_sum[car_num] - fees[0]) / fees[2]) * fees[3]
            answer.append(result)
    return answer


print(solution([180, 5000, 10, 600]	, ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10]	, ["00:00 1234 IN"]	))