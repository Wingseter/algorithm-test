board = []
R = 0
C = 0
K = 0
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
from collections import deque
'''
되돌아 볼 점
또 board에서 y, x 바꿔서 해서 햇갈렸다. 
step 에서 0으로 시작하는 것을 간과했다. 
조건을 제대로 파악하지 않았다. 출구는 출구만 했어야 했다. 따라서 마이너스를 통해 각각의 우주선을 구분해야 했다. 
위에 3을 추가해야하는것을 몰랐다. 진작에 깨우쳤어야 했다. 
조건을 잘못 적용해서 보드 초기화 조건이 잘못되었다. 

다음에는 이렇게 하자
무조건 그냥 y 먼저 x 다음이다. 
step은 무조건 1을 더한다. 
조건 문제 잘 읽자 
문제를 더 잘 읽자 
부등호를 다시 한번 생각하자 내 코드는 무조건 위가 작은거 아래가 큰거로 하자
'''
def spin_left(dir):
    return (dir - 1) % 4

def spin_right(dir):
    return (dir + 1) % 4

def find_next_action(x, y):
    global board, R, C
    real_x = x
    real_y = y

    check = [
        [(real_x, real_y + 2), (real_x - 1, real_y + 1), (real_x + 1, real_y + 1)], # down
        [(real_x - 2, real_y), (real_x - 1, real_y - 1), (real_x - 1, real_y + 1), (real_x - 2, real_y + 1), (real_x - 1, real_y + 2)], # left
        [(real_x + 2, real_y), (real_x + 1, real_y - 1), (real_x + 1, real_y + 1), (real_x + 2, real_y + 1), (real_x + 1, real_y + 2)], # right
    ]

    final_action = -1

    for positions in range(3):
        all_check = True
        for x, y in check[positions]:
            if x < 0 or x >= C or y < 0 or y >= R + 3:
                all_check = False
                break
            elif board[y][x] != 0:
                all_check = False
                break

        if all_check == True:
            final_action = positions
            break

    return final_action

def run_action(x, y, dir, action):
    if action == 0: # down
        nx = x
        ny = y + 1
        ndir = dir

    elif action == 1: # left
        nx = x - 1
        ny = y + 1
        ndir = spin_left(dir)

    elif action == 2:
        nx = x + 1
        ny = y + 1
        ndir = spin_right(dir)

    return nx, ny, ndir

def one_block_step(x, y, dir, k):
    nx = x
    ny = y
    ndir = dir
    while True:
        action = find_next_action(nx, ny)
        if action == -1:
            break
        nx, ny, ndir = run_action(nx, ny, ndir, action)

    for dir in range(4):
        fill_x = nx + dirs[dir][0]
        fill_y = ny + dirs[dir][1]
        if dir == ndir:
            board[fill_y][fill_x] = -k
        else:
            board[fill_y][fill_x] = k
    board[ny][nx] = k

    return nx, ny

def find_deepest_R(sx, sy):
    global board, R, C

    visited = [[False for _ in range(C)] for _ in range(R + 3)]
    q = deque()
    q.append((sy, sx))

    visited[sy][sx] = True

    deepest = 0
    while q:
        y, x = q.popleft()
        for dx, dy in dirs:
            ny, nx = y + dy, x + dx

            if nx < 0 or ny < 0 or nx >= C or ny >= R + 3:
                continue

            # 범위가 유효한 경우만 아래 조건을 실행
            if (board[y][x] < 0 and board[ny][nx] != 0) or (board[y][x] == board[ny][nx]) or board[y][x] == -board[ny][nx]:
                if not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

                    # save deepest
                    if ny > deepest:
                        deepest = ny
    return deepest


def clear_board():
    global board, R, C
    board = [[0] * C for _ in range(R + 3)] # C x R size

def print_board():
    global board
    y = len(board)
    x = len(board[0])

    for r in range(y):
        for c in range(x):
            print(board[r][c], end=" ")
        print("")

    print("-------")


def solution():
    global board, R, C, K
    clear_board()
    final_score = 0
    for step in range(K):
        xi, dir = map(int, input().split())
        xi -= 1
        yi = 1
        mid_x, mid_y = one_block_step(xi, yi, dir, step + 1)

        if mid_y < 4:
            clear_board()
        else:
            final_score += find_deepest_R(mid_x, mid_y) - 2

    return final_score



if __name__ == "__main__":
    R, C, K = map(int, input().split())
    answer = solution()
    print(answer)