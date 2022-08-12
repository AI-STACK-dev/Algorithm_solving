# 9월 15일 로그 데이터. / 초당 최대 처리량은 요청의 응답 완료 여부에 관계없이 임으이ㅢ 시간부터 1초간 처리하는 요청의 최
# 대 개수를 의미.

"""
lines -> n개의 로그, 응답완료시간s, 처리시간 T, 
처리시간 T 0.1s, 0.312s, 2s 

초당 최대 처리량을 리턴한다.
구간의 최대 값. 1초간 구간의 최대값.

여기서 포인트는 스타트포인트와 end point를 tuple로 정리하고, 어떻게 정렬한 후에,
어떻게 셀 것이냐. 이거임.

start_point, end point는 초단위 + * 1000해서 사용하면됨.
1초 <= 이것도 변환 단위 -->  1000

이게 정렬하고 난 다음에, O(n)으로 하는 방법 있었는데...
정렬도 필요없네 이미 정렬돼 있으니까. O(n^2)이라면 end 기준으로, 한칸씩 넘어가면서, -> log 길이가 2,000이라 n^2도 4백만
start < end + 1000이면 count 1 넘어가는 순간 break 후 다시 새로운 end point
"""
def solution(lines):
    answer = 0
    result = []
    n = len(lines)
    for line in lines:
        time, duration = line.split(' ')[1:]
        h, m, s = time.split(':')
        h = int(h) * 3600 * 1000
        m = int(m) * 60 * 1000
        s = float(s) * 1000

        duration = duration.split('s')[0]
        duration = float(duration) * 1000
        end_point = sum([h,m,s])
        start_point = end_point - duration + 1
        start_point, end_point = int(start_point), int(end_point)
        result.append((start_point, end_point)) # 이렇게 넣어도 end point를 기준으로 정렬된 상태
    
    # print(result)
    for i in range(n):
        s_start, s_end = result[i]
        cnt = 0
        for j in range(i, n):
            c_start, c_end = result[j]
            # print(s_start, s_end, c_start, c_end)
            if c_start < s_end + 1000:
                cnt +=1
        # print('\n')
        answer = max(answer, cnt)

    return answer
# lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
# print(solution(lines))

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