def str_to_int(time):
    h,m,s = time.split(':')
    return int(h)*3600 + int(m) * 60 + int(s)

def int_to_str(time):
    h = str(time // 3600)
    time = time % 3600
    m = str(time // 60)
    s = str(time % 60)
    return h.rjust(2, '0') + ':' + m.rjust(2, '0') + ':' + s.rjust(2, '0')

    
def solution(play_time, adv_time, logs):
    answer = ''
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    dp = [0 for _ in range(play_time + 1)]
    for log in logs:
        start, end = log.split('-')
        start, end = str_to_int(start), str_to_int(end)
        dp[start] +=1
        dp[end] -= 1
    
    for i in range(1, play_time+1):
        dp[i] = dp[i-1] + dp[i]
    
    for i in range(1, play_time+1):
        dp[i] = dp[i-1] + dp[i]
    max_index = -1
    max_time = -1
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if dp[i] - dp[i - adv_time] > max_time:
                max_time = dp[i] - dp[i - adv_time]
                max_index = i - adv_time + 1
        else:
            if dp[i] > max_time:
                max_time = dp[i]
                max_index = i - adv_time + 1
    return int_to_str(max_index)

print(solution("02:03:55"	, "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	))
print(solution("99:59:59", "25:00:00"	, ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00"	, "50:00:00"	 , ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	))