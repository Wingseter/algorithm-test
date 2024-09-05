word = input()
results = [-1] * 26
for index, letter in enumerate(word):
    if results[ord(letter) - 97] == -1:
        results[ord(letter) - 97] = index
for result in results:
    print(result, end=' ')
    