import sys; input = sys.stdin.readline;
while True:
    name, age_s, kg_s = input().rstrip().split()
    if name == '#':
        break
    age = int(age_s)
    kg = int(kg_s)
    print(name, end = ' ')
    if age <= 17 and kg < 80:
        print("Junior")
    else:
        print("Senior")