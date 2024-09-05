import math 

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist_bet = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif dist_bet == r1 + r2:
        print(1)
    elif dist_bet == abs(r1 - r2):
        print(1)
    elif dist_bet > r1 + r2:
        print(0)
    elif dist_bet < abs(r1 - r2):
        print(0)
    else:
        print(2)
  