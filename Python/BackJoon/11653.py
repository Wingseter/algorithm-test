N = int(input())

divider = 2
while N > 1:
    if N % divider == 0:
        N = N / divider
        print(divider)
    else:
        divider += 1