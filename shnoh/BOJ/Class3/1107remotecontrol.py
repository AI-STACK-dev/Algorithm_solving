import sys; input = sys.stdin.readline;
def solve(N, remain):
    digit = len(N)
    # 0일 경우...
    # 버튼 다 고장일 경우. 100에서 가야함...
    from_100 = abs(100 - int(N))
    if remain == set(): # 
        return from_100
    if remain == set([0]): # 
        return min(from_100, int(N) + 1)
    
    res = digit
    closest = 0
    for i in range(digit):
        value =  10 ** (digit - i - 1)
        num = int(N[i])
        diff = 0
        while True:
            # 아 망했다. 최종 숫자가... 그래서 브루트포스구나... 둘중 모든 경우를 고려해줘야...?
            if num + diff in remain:
                closest += value * (num + diff)
            elif num - diff in remain:
                closest += value * (num - diff)
            diff += 1
    
    return min(from_100, res)



N = input().rstrip()
m = int(input())
if m != 0:
    error = set(list(map(int, input().split())))
else:
    error = set()
remain = set([i for i in range(10)]) - error
print(solve(N, remain))


