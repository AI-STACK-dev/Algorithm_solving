import sys; input = sys.stdin.readline;
cnt = 1
data = ['Hole-in-one.', 'Double eagle.', 'Eagle.', 'Birdie.', 'Par.', 'Bogey.', 'Double Bogey.']
while True:
    p, s =  map(int, input().split())
    if p == 0:
        break
    print(f'Hole #{cnt}')
    cnt += 1
    if s == 1:
        print(data[0])
    else:
        print(data[min(6, 4 - (p - s))])
    print()