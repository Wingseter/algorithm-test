# reference: https://github.com/njw1204/LA-solutions
n, k = map(int, input().split())

dp = [[[0 for _ in range(3)] for _ in range(4)] for _ in range(n + 1)]
fix = [0] * (n + 1)

# first When the last day
# second Which pasta
# third How many dishes 
def culc_dp(day):
    for i in range(1, 4):
        if fix[day] != 0 and i != fix[day]:
            continue
        for j in range(1, 4):
            if i == j:
                dp[day][i][2] = dp[day -1][j][1]
            else:
                dp[day][i][1] += dp[day - 1][j][1] + dp[day - 1][j][2]
                dp[day][i][1] %= 10000


for _ in range(k):
    day, pasta = map(int, input().split())
    fix[day] = pasta

if fix[1] != 0:
    dp[1][fix[1]][1] = 1
else:
    dp[1][1][1] = 1
    dp[1][2][1] = 1
    dp[1][3][1] = 1

for day in range(2, n + 1):
    culc_dp(day)

sum = 0
for j in range(1, 4):
    for k in range(1, 3):
        sum += dp[n][j][k]

print(sum % 10000)

