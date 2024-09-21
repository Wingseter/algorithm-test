INF = 987654321
SWITCHES = 10
CLOCKS = 16

linked = [ # switch connect to clock
    # 01234567890012345
    "xxx.............",
    "...x...x.x.x....",
    "....x.....x...xx",
    "x...xxxx........",
    "......xxx.x.x...",
    "x.x...........xx",
    "...x..........xx",
    "....xx.x......xx",
    ".xxxxx..........",
    "...xxx...x...x..",

]

def areAlign(clocks):
    pass
def push(clocks, switch):
    for clock in range(CLOCKS):
        if linked[switch][clock] == 'x':
            clocks[clock] += 3
            if clocks[clock] == 15:
                clocks[clock] = 3

def solve(clocks, switch):
    if switch == SWITCHES:
        return 0 if areAlign(clocks) else INF
    ret = INF

    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, switch + 1))
        push(clocks, switch)

    return ret

