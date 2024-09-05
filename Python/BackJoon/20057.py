import sys
sys.stdin = open('sample.txt', "r")

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def rotate(boards):
    return [list(boards) for boards in reversed(tuple(zip(*boards)))]


def sand_storm(y, x, ny, nx, direction):
    sand_map = [[0] * 5 for _ in range(5)]

    sand_map[2][2] = board[ny][nx]

    # 5%
    sand_map[2][0] = board[ny][nx] // 20

    # 10%
    sand_map[1][1] = board[ny][nx] // 10
    sand_map[3][1] = board[ny][nx] // 10

    # 7%
    sand_map[1][2] = int(board[ny][nx] * 0.07)
    sand_map[3][2] = int(board[ny][nx] * 0.07)

    # 1%
    sand_map[1][3] = board[ny][nx] // 100
    sand_map[3][3] = board[ny][nx] // 100

    # 2%
    sand_map[0][2] = board[ny][nx] // 50
    sand_map[4][2] = board[ny][nx] // 50

    sand_map[2][1] = sand_map[2][2] - sand_map[2][0] - sand_map[1][1] \
                     - sand_map[3][1] - sand_map[1][2] - sand_map[3][2] \
                     - sand_map[1][3] - sand_map[3][3] - sand_map[0][2] \
                     - sand_map[4][2]

    for _ in range(direction):
        sand_map = rotate(sand_map)

    start_y = ny - 2
    start_x = nx - 2

    end_y = ny + 3
    end_x = nx + 3

    wasted = 0
    for index_y in range(start_y, end_y):
        for index_x in range(start_x, end_x):
            if index_y < 0 or index_y >= N or index_x < 0 or index_x >= N:
                wasted += sand_map[index_y - start_y][index_x - start_x]
                continue
            board[index_y][index_x] += sand_map[index_y - start_y][index_x - start_x]
    board[y][x] = 0

    return wasted


def simulation():
    y, x = N // 2 , N // 2
    direction = 0
    result = 0

    exit_flag = False
    for shift in range(1, N + 1, 1):
        for _ in range(2):
            for _ in range(shift):
                ny = y + dy[direction]
                nx = x + dx[direction]
                if ny < 0 or nx < 0:
                    exit_flag = True
                    break

                result += sand_storm(y, x, ny, nx, direction)

                y = ny
                x = nx
            if exit_flag:
                break
            direction += 1
            if direction == 4:
                direction = 0

        if exit_flag:
            break
    return result


print(simulation())