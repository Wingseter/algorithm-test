N = int(input())

result = 0
for _ in range(N):
    word = input()
    checker = set()
    temp = True
    before_letter = ''
    for letter in word:
        if letter != before_letter and letter in checker:
            temp = False
            break
        else:
            checker.add(letter)
        before_letter = letter
    if temp == True:
        result += 1

print(result)
    