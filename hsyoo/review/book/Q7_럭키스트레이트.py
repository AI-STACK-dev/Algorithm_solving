def solution(n):
    length = len(n)
    left = n[:length//2]
    right = n[length//2:]
    l_sum = sum(list(map(int, list(left))))
    r_sum = sum(list(map(int, list(right))))
    if l_sum == r_sum:
        return 'LUCKY'
    else:
        return 'READY'

n = input()
print(solution(n))