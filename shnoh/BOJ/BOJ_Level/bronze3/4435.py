import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    data1 = list(map(int, input().split()))
    data2 = list(map(int, input().split()))
    res1 = data1[0] + 2 * data1[1] + 3 * (data1[2] + data1[3]) + 4 * data1[4] + 10 * data1[5]
    res2 = data2[0] + 2 * (data2[1] + data2[2] + data2[3]) + 3 * data2[4] + 5 * data2[5] + 10 * data2[6]
    print(f'Battle {i + 1}: ', end = '')
    if res1 > res2:
        print("Good triumphs over Evil")
    elif res1 < res2:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")    