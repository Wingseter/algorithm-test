N = int(input())
strings = []
scores = [0] * N
for i in range(N):
    strings.append(input())

for index, string in enumerate(strings):
    score = 1
    for word in string:
        if word == "O":
            scores[index] += score
            score += 1
        else:
            score = 1

for score in scores:
    print(score)
