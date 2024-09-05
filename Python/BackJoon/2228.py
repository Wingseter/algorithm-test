n, m = map(int, input().split())
nums = list()

for _ in range(n):
    nums.append(int(input()))

max = -1
for i in range(0, n - m + 1):
    total = sum(nums[i: i + m + 1])
    if total > max:
        max = total

print(max)


