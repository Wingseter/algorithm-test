import math

def is_numeric(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())
nums = list(map(int, input().split()))

counter = 0
for num in nums:
    if is_numeric(num):
        counter += 1

print(counter)

