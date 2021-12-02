data = list(map(int,input().split()))
if data == list(range(1,9)):
    print("ascending")
elif data == list(range(1,9))[::-1]:
    print("descending")
else:
    print("mixed")