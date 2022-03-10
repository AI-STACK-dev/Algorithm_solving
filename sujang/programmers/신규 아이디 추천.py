def solution(new_id):
    # step1
    new_id = new_id.lower()
    # step2
    ans = ''
    for c in new_id:
        if c.isalnum() or c in "-_.":
            ans += c
    # step3
    while ".." in ans:
        ans = ans.replace("..",".")
    # step4
    ans = ans[1:] if ans[0]=='.' and len(ans) > 1 else ans
    ans = ans[:-1] if ans[-1] == '.' else ans
    # step5
    ans = "a" if len(ans) == 0 else ans
    # step6
    if len(ans) >= 16:
        ans = ans[:15]
        if ans[-1] =='.':
            ans = ans[-1:]
    # step7
    if len(ans) <= 2:
        ans += ans[-1]*(3-len(ans))
    return ans
