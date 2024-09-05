import math

n = 123456 * 2
array = [True for i in range(n + 1)]
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] is True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

while True:
    num = int(input())
    if num == 0:
        break
    else:
        start_num = num
        end_num = 2 * num
        counter = 0
        for i in range(start_num + 1, end_num + 1):
            if array[i] == True:
                counter += 1
        print(counter)

