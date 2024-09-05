import sys
sys.stdin = open('python/sample.txt', "r")

from copy import deepcopy

board = list()
fish_index = [0] * 17
fish_index[0] = -1

for y in range(4):
    line = list()
    input_lane = list(map(int, input().split()))
    fish_num = input_lane[0::2]
    fish_dir = input_lane[1::2]

    for x, fish_data in enumerate(zip(fish_num, fish_dir)):
        line.append(fish_data)
        fish_index[fish_data[0]] = [y, x]
    board.append(line)

dx = [0,  0, -1, -1, -1, 0, 1, 1,  1]
dy = [0, -1, -1,  0,  1, 1, 1, 0, -1]

# 방향 전환
def get_available_dir(y, x, direction, skark_y, shark_x):
    while (y + dy[direction] <= -1 or y + dy[direction] >=4 or x + dx[direction] <= -1 or x + dx[direction] >= 4) or (y + dy[direction] == skark_y and x + dx[direction] == shark_x): 
        direction += 1
        if direction > 8:
            direction = 1
    return direction

# 모든 물고기 움직인다.
def all_fish_move(_board, _fish_index, shark_y, shark_x):
    for fish_num in range(len(_fish_index)):
        index = _fish_index[fish_num]
        if index == -1:
            continue
        else:
            fish = _board[index[0]][index[1]]
            fish_num = fish[0]
            fish_dir = fish[1]

            next_dir = get_available_dir(index[0], index[1], fish_dir, shark_y, shark_x)
            next_fish = (fish_num, next_dir)

            ny = index[0] + dy[next_dir]
            nx = index[1] + dx[next_dir]

            if _board[ny][nx] != 0:
                change_fish_num = _board[ny][nx][0]
                _fish_index[fish_num], _fish_index[change_fish_num] = _fish_index[change_fish_num], _fish_index[fish_num]
            else:
                _fish_index[fish_num] = [ny, nx]
            _board[index[0]][index[1]], _board[ny][nx] = _board[ny][nx], next_fish 

# 가능한 상어 움직임 경우 반환
def get_shark_available_move(_board, y, x, direction):
    available = []
    ny = y + dy[direction]
    nx = x + dx[direction]
    while ny > -1 and ny < 4 and nx > -1 and nx < 4:
        if _board[ny][nx] != 0:
            available.append((ny, nx))
        ny += dy[direction]
        nx += dx[direction]
        
    return available
            
# shark first eat initialize
fish_eaten = board[0][0]

shark_index = fish_index[fish_eaten[0]]
fish_index[fish_eaten[0]] = -1

max_count = fish_eaten[0]

shark_dir = fish_eaten[1]
# -2 = shark 0 = empty
board[0][0] = -2

global biggest
biggest = -1

# 시뮬레이션 스타트
def dfs(_board, _fish_index, y, x, shark_dir, max_count):
    all_fish_move(_board, _fish_index, y, x)

    available_move = get_shark_available_move(_board, y, x, shark_dir)

    if len(available_move) == 0:
        global biggest
        if max_count > biggest:
            biggest = max_count
    else:
        for new_y, new_x in available_move:
            fish_eaten = _board[new_y][new_x]

            new_board = deepcopy(_board)
            new_fish_index = deepcopy(_fish_index)

            new_fish_index[fish_eaten[0]] = -1

            shark_dir = fish_eaten[1]
            # -2 = shark 0 = empty
            new_board[y][x] = 0
            new_board[new_y][new_x] = -2
            dfs(new_board, new_fish_index, new_y, new_x, shark_dir, max_count + fish_eaten[0])

dfs(board, fish_index, shark_index[0], shark_index[1], shark_dir, max_count)
print(biggest)
