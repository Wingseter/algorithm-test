while True:
    lines = list(map(int, input().split()))
    lines.sort()
    if lines[0] == 0 and lines[1] == 0 and lines[2] == 0:
        break
    elif lines[0] == 0 or lines[1] == 0 or lines[2] == 0:
        print('wrong')
    elif lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2:
        print('right')
    else:
        print('wrong')