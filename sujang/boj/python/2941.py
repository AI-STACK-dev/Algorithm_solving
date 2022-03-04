d = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()
for i in d:
    word = word.replace(i, '*')
print(len(word))
