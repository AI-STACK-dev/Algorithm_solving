import sys; input = sys.stdin.readline;
yut = ['E','A','B','C','D']
yut.reverse()
for _ in range(3):
    data = list(map(int, input().split()))
    print(yut[sum(data)])