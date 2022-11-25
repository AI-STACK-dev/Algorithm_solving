def solution(alp, cop, problems):
    answer = 0
    INF = int(1e9)
    alp_list = [x[0] for x in problems]
    cop_list = [x[1] for x in problems]
    target_alp = max(alp_list)
    target_cop = max(cop_list)

    alp = min(alp, target_alp)
    cop = min(cop, target_cop)
    dp = []
    for _ in range(target_alp + 1):
        temp = [INF for _ in range(target_cop + 1)]
        dp.append(temp)
    dp[alp][cop] = 0
    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            if i + 1 <= target_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j + 1 <= target_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    n_alp = min(i + alp_rwd, target_alp)
                    n_cop = min(j + cop_rwd, target_cop)
                    dp[n_alp][n_cop] = min(dp[n_alp][n_cop], dp[i][j] + cost)

    answer = dp[-1][-1]
    return answer

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]	))