def check(answer):
    for x,y,wht in answer:
        # 기둥 설치의 경우
        if wht == 0:
            if y == 0 or [x,y-1,0] in answer or [x,y,1] in answer or [x-1,y,1] in answer:
                continue
            return False
        # 보 설치의 경우
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, f):
    ans = []
    for x,y,typ,wht in f:
        # 삭제의 경우
        if wht == 0:
            ans.remove([x,y,typ])
            if not check(ans):
                ans.append([x,y,typ])
        # 삽입의 경우
        else:
            ans.append([x,y,typ])
            if not check(ans):
                ans.remove([x,y,typ])
    return sorted(ans)