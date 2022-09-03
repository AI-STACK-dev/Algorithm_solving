import sys; input = sys.stdin.readline;
while True:
    a, b = input().rstrip().split()
    if a == "00:00":
        break
    sh, sm = map(int, a.split(':'))
    dh, dm = map(int, b.split(':'))

    sm += dm
    sh += sm // 60
    sm = sm % 60

    sd = 0
    sh += dh
    sd += sh // 24
    sh = sh % 24
    print(f'{str(sh).zfill(2)}:{str(sm).zfill(2)}', end = ' ')
    if sd > 0:
        print(f'+{sd}')
    else:
        print()