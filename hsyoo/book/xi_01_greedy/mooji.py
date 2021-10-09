def solution(food_times, k):
    idx = 0
    n = len(food_times)
    while True:
        if food_times[idx%n] > 0:
            food_times[idx%n] -= 1
            k-=1
            idx+=1
        elif k==0:
            break
        else:
            idx+=1
    print(food_times)
    if sum(food_times) <=0:
        return -1
    for i in range(n):
        if food_times[(idx+i)%n] > 0:
            return (idx+i)%n
        else:
            continue
    answer = 0
    return answer
food_times, k = input().split(']')
k = int(list(k)[-1])

food_times=food_times.split(',')
ary = []
for idx in range(len(food_times)):
    ary.append(int(list(food_times[idx])[1]))
print(ary, k)
print(solution(ary, k)+1)