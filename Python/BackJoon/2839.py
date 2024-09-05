N = int(input())
bucket = [-1] * (N + 1)
bucket[0] = 0

for five in range(1001):
    for three in range(1667):
        index = five * 5 + three * 3
        if index > N:
            break
        else:
            if bucket[index] == -1 or \
                    bucket[index] > five + three:
                bucket[index] = five + three

print(bucket[N])

