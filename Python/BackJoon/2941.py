word = input()
table = ["c=","c-","dz=","d-","lj","nj", "s=","z="]

for value in table:
    word = word.replace(value, '$')

print(len(word))