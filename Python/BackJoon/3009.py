result_x, result_y = 0, 0

for _ in range(3):
    x, y = map(int, input().split())
    result_x ^= x
    result_y ^= y

print(f"{result_x} {result_y}")





