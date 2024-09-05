import math

def is_numeric(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())

numeric_nums = []
for num in range(M, N+ 1):
    if is_numeric(num):
        numeric_nums.append(num)
if len(numeric_nums) == 0:
    print(-1)
else:
    print(sum(numeric_nums))
    print(min(numeric_nums))


