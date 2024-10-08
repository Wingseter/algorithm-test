board = []
fill = []
K = 0
M = 0

dir = [[1,0],[0,1],[-1,0],[0,-1]]

'''
문제 정의 

처음부터 문제 제대로 안읽어서 엉뚱하게 짰음 
모든 것을 다했어야 했는데 가운데 3개만 돌림
처음부터 다 갈아 엎어야 했음 그렇다보니 기존의 코드에 떡칠을 하게 되고 
결국에 망함 이게 페턴임 
너의 문제는 문제를 재대로 안읽는다는것

돌릴때 실수 하지마 
덮어 씌어진다

행렬 조건도 제데로 판단 안했어 또 문제 재대로 안읽었어 아니 읽었는데 구현 안했어 

destroy 에서 맨탈 나갔어 
생각보다 쉬운 방법으로 해결해야했어 연쇄 폭발은 그냥 score 만 더하면 되는거였는데

이거 시험이었으면 무조건 틀렸다. 
진짜 최악이었어 너

'''

from collections import deque

candidate_board = [[[0] * 5 for _ in range(5)] for _ in range(3 * 3 * 3)] # 90 # 180 # 270
candidate_index = 0
before_candidate_index = candidate_index

def print_board(board):
    for i in range(5):
        for j in range(5):
            print(board[i][j], end=" ")
        print("")

    print("------------")

def get_candidate_index():
    global candidate_index
    temp = candidate_index
    candidate_index += 1
    return temp

def set_candidate_index(index):
    global candidate_index
    candidate_index = index

def copy_board(select):
    for y in range(5):
        for x in range(5):
            board[y][x] = candidate_board[select][y][x]

def calculate_score(select_index):
    select_board = candidate_board[select_index]
    visited = [[False for _ in range(5)] for _ in range(5)]
    total_score = 0

    for sel_y in range(5):
        for sel_x in range(5):
            if visited[sel_y][sel_x]:
                continue

            q = deque()
            path = []

            q.append((sel_y, sel_x))
            visited[sel_y][sel_x] = True
            path.append((sel_y, sel_x))

            count_same = 1

            while q:
                y, x = q.popleft()

                for my, mx in dir:
                    ny = y + my
                    nx = x + mx

                    if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                        continue

                    if select_board[ny][nx] == select_board[y][x] and not visited[ny][nx] :
                        visited[ny][nx] = True
                        count_same += 1
                        q.append((ny, nx))
                        path.append((ny, nx))

            if count_same >= 3:
                total_score += count_same
                for del_y, del_x in path:
                    select_board[del_y][del_x] = -1


    for x in range(5):
        for y in range(4, -1, -1):
            if select_board[y][x] == -1:
                select_board[y][x] = fill[get_candidate_index()]

    return total_score


def rotate_3x3(original, target, s_y, s_x):
    M = 5

    for y in range(M):
        for x in range(M):
            target[y][x] = original[y][x]


    for y in range(s_y, s_y + 3):
        for x in range(s_x, s_x + 3):
            # move to center
            oy, ox = y - s_y, x - s_x
            # rotate
            ry, rx = ox, 3 - oy - 1
            # final move to origin
            cy, cx = ry + s_y, rx + s_x
            #  3x3 rotate
            target[cy][cx] = original[y][x]


def prepare_rotate():
    for s_y in range(3):
        for s_x in range(3):
            for rotate in range(3):
                if rotate == 0: # first
                    rotate_3x3(board, candidate_board[s_y * 9 + s_x * 3 + rotate], s_y, s_x)
                else:
                    rotate_3x3(candidate_board[s_y * 9 + s_x * 3 + rotate - 1], candidate_board[s_y * 9 + s_x * 3 + rotate], s_y, s_x)

def find_biggest_score():
    global board, candidate_board, before_candidate_index

    biggest_index = -1
    biggest_score = -1
    smallest_angle = 100

    prepare_rotate()
    for s_x in range(3):
        for s_y in range(3):
            for rotate in range(3):
                score = calculate_score(s_y * 9 + s_x * 3 + rotate)

                if score > biggest_score or (score == biggest_score and rotate < smallest_angle):
                    smallest_angle = rotate
                    biggest_score = score
                    biggest_index = s_y * 9 + s_x * 3 + rotate

                set_candidate_index(before_candidate_index)

    score = biggest_score
    set_candidate_index(before_candidate_index + biggest_score)

    while score != 0:
        score = calculate_score(biggest_index)
        biggest_score += score

    before_candidate_index += biggest_score
    set_candidate_index(before_candidate_index)
    return biggest_score, biggest_index

def solution():
    global board, fill, K, M

    total_score = []

    for step in range(K):
        biggest_score, biggest_index = find_biggest_score()
        if biggest_score == 0:
            break
        copy_board(biggest_index) # copy with filling empty
        total_score.append(biggest_score)

    return total_score

if __name__ == '__main__':
    K, M = map(int, input().split())

    for _ in range(5):
        board.append(list(map(int, input().split())))

    fill = list(map(int, input().split()))

    answer = solution()
    print(" ".join(map(str, answer)))


