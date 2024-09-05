N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    app_x, app_y = map(int, input().split())
    board[app_x - 1][app_y - 1] = 2

T = int(input())
change_y = [-1, 0, 1, 0]
change_x = [0, 1, 0, -1]


def is_collide(y, x):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    elif board[y][x] == 1:
        return True
    return False


def change_dir(direction, flag):
    if flag == 'L':
        direction -= 1
        if direction == -1:
            direction = 3
    else:
        direction += 1
        if direction == 4:
            direction = 0
    return direction


counter = 0
head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
now_dir = 1
tail_list = []
board[head_y][head_x] = 1
prev_range = 0
flag = True

commend_time = list()
commend_key = list()

for _ in range(T):
    input_range, input_dir = input().split()
    commend_time.append(int(input_range))
    commend_key.append(input_dir)
key_in_progress = 0

while flag:
    ny = head_y + change_y[now_dir]
    nx = head_x + change_x[now_dir]
    counter += 1
    if is_collide(ny, nx):
        flag = False
        break
    else:
        tail_list.append(now_dir)
        if board[ny][nx] != 2:
            board[tail_y][tail_x] = 0
            tail_dir = tail_list.pop(0)
            tail_y += change_y[tail_dir]
            tail_x += change_x[tail_dir]

        board[ny][nx] = 1
        head_y, head_x = ny, nx
    if T > key_in_progress and counter == commend_time[key_in_progress]:
        now_dir = change_dir(now_dir, commend_key[key_in_progress])
        key_in_progress += 1
print(counter)
