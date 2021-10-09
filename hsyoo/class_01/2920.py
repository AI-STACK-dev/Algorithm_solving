ary = list(map(str, input().split()))
str_ = ary[0]
for case in ary[1:]:
    str_ += case
if str_ == "12345678":
    print("ascending")
elif str_ == "87654321":
    print("descending")
else:
    print("mixed")