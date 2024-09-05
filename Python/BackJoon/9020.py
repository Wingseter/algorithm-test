import math

n = 10000
array = [True for i in range(n + 1)]
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] is True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
T = int(input())

for _ in range(T):
    num = int(input())

    result1, result2 = 0, 0
    for first in range(int(num/2) + 1):
        if array[first] == True and array[num - first] == True:
            result1, result2 = first, num - first
    print(f"{result1} {result2}")