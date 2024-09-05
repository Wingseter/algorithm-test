N = int(input())
board = [['*'] * N for _ in range(N)]

def star(start_x, start_y, num):
    if num == 1:
        return
    div_num = int(num / 3)
    for y in range(div_num, div_num * 2):
        for x in range(div_num, div_num * 2):
            board[start_y + y][start_x + x] = ' '
    for y in range(3):
        for x in range(3):
            star(start_y + y * div_num, start_x + x * div_num, div_num)
    

star(0, 0, N)
for line in board:
    print(''.join(line))