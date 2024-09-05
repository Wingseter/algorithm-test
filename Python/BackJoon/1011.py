T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    dist = Y - X

    start_point = 1
    adder = 1
    result = 1
    doubler = 1
    while start_point <= dist:
        start_point += adder
        if doubler != 1:
            adder += 1
        doubler *= -1
        result += 1

    print(result - 1)




