N = int(input())

def check_hansu(num):
    divide = list(map(int, str(num)))
    size = len(divide)
    if size <= 2:
        return True
    else:
        pointer = 0
        while pointer < size - 2:
            if divide[pointer + 1] - divide[pointer] \
                != divide[pointer + 2] - divide[pointer + 1]:
                return False
            pointer += 1
        return True

counter = 0
for num in range(1, N+1):
    if check_hansu(num) == True:
        counter += 1

print(counter)


