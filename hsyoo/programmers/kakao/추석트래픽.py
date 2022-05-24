def solution(lines):
    table = []
    n = len(lines)
    for line in lines:
        t = 0 
        _, time, during = line.split()
        h, m, s = time.split(':')
        t += int(h)*60*60*1000
        t += int(m) * 60 * 1000
        t += int(float(s) * 1000)
        during = int(float(during[:-1]) * 1000)
        start = t - during + 1
        end = t

        table.append((start, end))
    # table.sort(key = lambda x : x[1])
    answer = 1
    for i in range(n):
        t1 = 0
        start = table[i][0]
        end = table[i][1]
        for j in range(i,n):
            if table[j][0] - 1000 < end:
                t1 +=1
        answer = max(answer, t1)

    return answer


lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))
lines = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

print(solution(lines))
lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]


print(solution(lines))