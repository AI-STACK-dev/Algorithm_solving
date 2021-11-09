def solve(first, last, k):
    first_set = set(first)
    last_set = set(last) - first_set

    first_sum = sum(first_set)
    last_sum = sum(last_set)
    if first_sum == last_sum:
        print(-1)
        return
    elif first_sum > last_sum:
        print(first_sum)
        loser_card = sorted(list(last_set))
    else:
        print(last_sum)
        loser_card = sorted(list(first_set))
    for i in loser_card:
        print(i, end = ' ')

winner = input()
n, m = map(int, input().split()) # 미 사용
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if winner == 'A':
    solve(A, B, m)
else: 
    solve(B,A, n)