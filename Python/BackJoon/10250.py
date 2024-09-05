import math
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    flore= N % H
    if flore == 0:
        flore = H
    room = math.ceil(N / H)
    print("{0}{1:02d}".format(flore, room))



