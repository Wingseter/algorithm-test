N = int(input())

big = []

for count in range(N):
    data = list(map(int , input().split()))
    big.append(data)

result = [1] * N

for i in range(N):
    for j in range(N):
        if big[i][0] < big[j][0] and \
            big[i][1] < big[j][1]:
            result[i] += 1

for i in result:
    print(i)
