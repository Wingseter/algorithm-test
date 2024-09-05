def solution(dartResult):
    answer = 0
    numbers = "1234567890"
    letters = "SDT"
    
    score = []
    prev = ""
    for letter in dartResult:
        if letter in numbers:
            prev += letter
        elif letter in letters:
            if letter == "S":
                prev = int(prev) ** 1
            elif letter == "D":
                prev = int(prev) ** 2
            elif letter == "T":
                prev = int(prev) ** 3
            score.append(prev)
            prev = ""
        elif letter == "*":
            if len(score) == 1:
                score[0] *= 2
            else:
                score[-2] *= 2
                score[-1] *= 2
        elif letter == "#":
            score[-1] *= -1
    answer = sum(score)
    return answer