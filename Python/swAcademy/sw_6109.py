import sys
sys.stdin = open('sample_input.txt', "r")

T = int(input())

for test_case in range(1, T + 1):
    n, direction = input().split()
    n = int(n)
    board = [list(map(int, input().split())) for _ in range(n)]
    
    start = 0
    end = 0
    x_offset = 0
    y_offset = 0    

    if direction == "up":
        y_offset = -1
        end = n
    elif direction == "down":
        y_offset = 1
        start = n - 1
        end = -1
    elif direction == "right":
        x_offset = 1
        start = n - 1
        end = -1  
    elif direction == "left":
        x_offset = -1
        end = n

    
    if direction == "up" or direction == "down":      
        for y in range(start - y_offset, end, -y_offset):
            for x in range(0, n):
                if board[y][x] == 0:
                    continue

                target_y = y + y_offset
                while board[target_y][x] == 0:
                    target_y += y_offset
                    if target_y < 0:
                        target_y = 0
                        break
                    elif target_y >= n:
                        target_y = n - 1
                        break

                if board[y][x] == board[target_y][x]:
                    board[target_y][x] *= 2
                    board[target_y - y_offset][x] = -1
                    if target_y - y_offset != y:
                        board[y][x] = 0
                elif board[target_y][x] == 0 or board[target_y][x] == -1:
                    board[target_y][x] = board[y][x]
                    board[y][x] = 0
                else:
                    board[target_y - y_offset][x] = board[y][x]
                    if target_y - y_offset != y:
                        board[y][x] = 0

    elif direction == "right" or direction == "left":
        for x in range(start - x_offset, end, -x_offset):
            for y in range(0, n):
                if board[y][x] == 0:
                    continue

                target_x = x + x_offset
                while board[y][target_x] == 0:
                    target_x += x_offset
                    if target_x < 0:
                        target_x = 0
                        break
                    elif target_x >= n:
                        target_x = n - 1
                        break

                if board[y][x] == board[y][target_x]:
                    board[y][target_x] *= 2
                    board[y][target_x - x_offset] = -1
                    if target_x - x_offset != x:
                        board[y][x] = 0
                elif board[y][target_x] == 0 or board[y][target_x] == -1:
                    board[y][target_x] = board[y][x]
                    board[y][x] = 0
                else:
                    board[y][target_x - x_offset] = board[y][x]
                    if target_x - x_offset != x:
                        board[y][x] = 0

    for y in range(n):
        for x in range(n):
            if board[y][x] == -1:
                board[y][x] = 0

    print(f"#{test_case}")    
    for line in board:
        print(" ".join(map(str, line)))