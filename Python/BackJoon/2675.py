T = int(input())
result = []
for i in range(T):
    R, word = input().split()
    new_word = str()
    for letter in word:
        new_word = new_word + (letter * int(R))
    result.append(new_word)

for line in result:
    print(line)