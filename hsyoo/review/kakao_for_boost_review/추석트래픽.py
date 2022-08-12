#초당 최대 처리량 계산, :요청의 응답 완료 여부에 관계없이 임의 시간부터 1초간 처리하는 요청의 최대 개수
#lines 배열은 S를 기준으로 오름차순 정렬

def solution(lines):
    answer = 0
    n = len(lines)
    result = []
    for line in lines:
        _, time, duration = line.split()
        h, m, s = time.split(':')
        h = int(h) * 3600 * 1000
        m = int(m) * 60 * 1000
        s = int(float(s) * 1000)
        duration = int(float(duration[:-1]) * 1000)
        end_point = sum([h, m ,s])
        start_point = end_point - duration + 1
        result.append((start_point, end_point))
        
    for i in range(n):
        cnt = 0
        s_start, s_end = result[i]
        for j in range(i, n):
            c_start, c_end = result[j]
            if s_end + 1000 > c_start:
                cnt += 1
        answer = max(answer, cnt)
    return answer


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