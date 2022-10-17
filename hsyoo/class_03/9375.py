from collections import defaultdict
T = int(input())
for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        name, type_ = input().split()
        clothes[type_] += 1
    answer = 1
    for key_ in clothes.keys():
        answer *= (clothes[key_] + 1)
    print(answer - 1)
        