import math
A, B, V = map(int, input().split())

min_last = V - A
result = min_last / (A - B)
result = math.ceil(result) + 1

print(result)
