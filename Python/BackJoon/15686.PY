def Brute_Force(idx, x, y):
    global answer
    if(idx == m):
        choice_chicken = []
        for i in range(n):
            for j in range(n):
                if(City[i][j] == 3):
                    choice_chicken.append((i,j))
        res = Min_Distance(choice_chicken, house)
        if(answer > sum(res)):
            answer = sum(res)
    else:
        for i in range(x, n):
            if(i == x): k = y
            else: k = 0
            for j in range(k, n):
                if(City[i][j] == 2):
                    City[i][j] = 3
                    Brute_Force(idx + 1, i, j + 1)
                    City[i][j] = 2

def Min_Distance(chicken, house):
    sum_distance = []
    for i in house:
        min_D = 987654321
        for j in chicken:
            Distance = abs(i[0]-j[0]) + abs(i[1]- j[1])
            min_D = min(min_D, Distance)
        sum_distance