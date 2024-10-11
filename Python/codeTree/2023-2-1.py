N, M, P, C, D = 0, 0, 0, 0, 0
board = []  # left top 1, 1
santa_position = []
santa_status = []

dolph_position = []
INF = 987654321
update_list = []
santa_scores = []

dir_8 = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]  # 4 for line 4 for cross

now_turn = 0

'''
또 문제 안읽어서 상우하좌 이거 고려 안했죠?
망할 스턴 계산 잘못했죠 그러니까 같은 계산은 하나에 모아서 했어야죠
방향 계산에서 나머지 구할때 오타 났는데 이거 하나 때문에 몇시간 버렸죠? 너무 슬프죠?

'''

def print_board(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            print(board[y][x], end=" ")
        print(" ")

    print("------------------")
    pass


def update_dolph(move_y, move_x):
    old_dolph_y, old_dolph_x = dolph_position
    board[old_dolph_y][old_dolph_x] = 0  # make it empty
    board[move_y][move_x] = -1

    dolph_position[0] = move_y
    dolph_position[1] = move_x


def activate_dolph_move(target_santa, select_dir):
    dol_y, dol_x = dolph_position
    move_y = dol_y + dir_8[select_dir][0]
    move_x = dol_x + dir_8[select_dir][1]

    if board[move_y][move_x] != 0:  # if santa there
        activate_santa_move(target_santa, select_dir, C)
        santa_scores[target_santa] += C
        if santa_status[target_santa] != -1:
            santa_status[target_santa] = 2
        print(f"Santa {target_santa} Move {select_dir}")
        print(santa_scores)

    update_dolph(move_y, move_x)


def move_dolph():
    closest = INF
    dol_y, dol_x = dolph_position
    target_santa = -1
    biggest_y = -1
    biggest_x = -1

    for i in range(1, P + 1):
        if santa_status[i] == -1:
            continue
        santa_y, santa_x = santa_position[i]
        dist = calculate_distance(santa_y, dol_y, santa_x, dol_x)
        if dist < closest or (
                dist == closest and (santa_y > biggest_y or (santa_y == biggest_y and santa_x > biggest_x))):
            closest = dist
            target_santa = i
            biggest_y = santa_y
            biggest_x = santa_x

    target_y, target_x = santa_position[target_santa]

    smallest_dist = INF
    select_direction = -1
    for direct in range(8):
        ny = dol_y + dir_8[direct][0]
        nx = dol_x + dir_8[direct][1]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue

        calc_dist = calculate_distance(target_y, ny, target_x, nx)
        if calc_dist < smallest_dist:
            smallest_dist = calc_dist
            select_direction = direct

    activate_dolph_move(target_santa, select_direction)


def update_santa(santa, move_y, move_x):
    old_santa_y, old_santa_x = santa_position[santa]
    board[old_santa_y][old_santa_x] = 0
    board[move_y][move_x] = santa

    santa_position[santa][0] = move_y
    santa_position[santa][1] = move_x


def oposite_direction(direction):
    if direction % 4 < 2:
        return direction + 2
    else:
        return direction - 2


def activate_santa_move(santa, direction, step):  # special event 0: noting 1: crash by santa, 2: crash by dolph
    if step == 0:
        return

    santa_pos_y, santa_pos_x = santa_position[santa]
    change_y = dir_8[direction][0] * step
    change_x = dir_8[direction][1] * step

    move_y = santa_pos_y + change_y
    move_x = santa_pos_x + change_x
    im_crashed = False

    if move_y < 0 or move_y >= N or move_x < 0 or move_x >= N:
        santa_status[santa] = -1
        board[santa_pos_y][santa_pos_x] = 0
        return True

    if board[move_y][move_x] < 0:  # if dolph there
        santa_status[santa] = 1
        activate_santa_move(santa, oposite_direction(direction), D - 1)  # it hit by moving so it means hit by himself
        im_crashed = True
        santa_scores[santa] += D
        print(santa_scores)

    elif board[move_y][move_x] > 0:  # if santa there
        im_crashed = activate_santa_move(board[move_y][move_x], direction, 1)

    if not im_crashed:
        update_santa(santa, move_y, move_x)


def move_santa():
    target_y, target_x = dolph_position

    for santa_num in range(1, P + 1):
        if santa_status[santa_num] == -1:  # drop
            continue
        elif santa_status[santa_num] > 0:  # stun
            print(santa_num, "Cant Move")
            santa_status[santa_num] -= 1
            continue

        santa_y, santa_x = santa_position[santa_num]

        smallest_dist = INF
        select_dir = -1

        original_dist = calculate_distance(target_y, santa_y, target_x, santa_x)

        for dirs in range(4):
            dy, dx = dir_8[dirs]
            my = santa_y + dy
            mx = santa_x + dx

            if my < 0 or my >= N or mx < 0 or mx >= N:
                continue

            if board[my][mx] > 0:
                continue

            dist = calculate_distance(my, target_y, mx, target_x)
            if dist < smallest_dist:
                smallest_dist = dist
                select_dir = dirs
        if select_dir == -1 or original_dist < smallest_dist:
            continue

        activate_santa_move(santa_num, select_dir, 1)
        print(f"Santa {santa_num} moved to {select_dir}")
        print_board(board)

    for santa_num in range(1, P + 1):
        if santa_status[santa_num] >= 0:
            santa_scores[santa_num] += 1


def calculate_distance(R_1, R_2, C_1, C_2):  # R is y C is X
    return (R_1 - R_2) ** 2 + (C_1 - C_2) ** 2


def solve():
    global now_turn

    print(f"C is {C} D is {D}")
    print_board(board)
    for turn in range(1, M + 1):
        print("This turn is", turn)
        now_turn = turn
        move_dolph()
        print_board(board)
        move_santa()
        print_board(board)

        print(" ".join(map(str, santa_scores[1:])))


def initialize(_n, _m, _p, _c, _d):
    global board, N, M, P, C, D, dolph_position, santa_position, now_turn, santa_status, santa_scores
    N, M, P, C, D = _n, _m, _p, _c, _d  # M : Turn, P : santa_count, c: doph power, d: santa_power
    board = [[0] * N for _ in range(N)]

    ry, rx = list(map(int, input().split()))
    ry -= 1
    rx -= 1
    dolph_position = [ry, rx]
    board[ry][rx] = -1

    santa_position = [[] for _ in range(P + 1)]
    santa_status = [0] * (P + 1)  # 0 : normal 1: stun 2: drop
    santa_scores = [0] * (P + 1)

    now_turn = 0

    for i in range(P):
        pn, py, px = list(map(int, input().split()))
        py -= 1
        px -= 1
        santa_position[pn].append(py)
        santa_position[pn].append(px)
        board[py][px] = pn


if __name__ == '__main__':
    N, M, P, C, D = list(map(int, input().split()))
    initialize(N, M, P, C, D)
    solve()
