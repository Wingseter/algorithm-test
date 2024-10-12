# import sys
# sys.stdin = open("input.txt", "r")

L, N, Q = 0, 0, 0
board = []
knight = []

knight_info = []
from collections import deque

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)] # 상우하좌, 안움직임

def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
        print(" ")

    print("----------------")

def remove_knight_board(knight_num):
    global knight
    global knight_info

    sel_knight = knight_info[knight_num]

    for y in range(sel_knight['y'], sel_knight['y'] + sel_knight['h']):
        for x in range(sel_knight['x'], sel_knight['x'] + sel_knight['w']):
            knight[y][x] = 0

def place_knight_board(knight_num, direct):
    sel_knight = knight_info[knight_num]

    new_y = sel_knight['y'] + dirs[direct][0]
    new_x = sel_knight['x'] + dirs[direct][1]

    for y in range(new_y, new_y + sel_knight['h']):
        for x in range(new_x, new_x + sel_knight['w']):
            if knight[y][x] != 0:
                assert "ERROR moving"
            knight[y][x] = knight_num

    knight_info[knight_num]['y'] = new_y
    knight_info[knight_num]['x'] = new_x

def initialize():
    global L, N, Q, board, knight, knight_info
    knight = [[0] * (L + 2) for _ in range(L + 2)]

    # board information
    board.append([2] * (L + 1))
    for i in range(1, L + 1):
        board.append([2] + list(map(int, input().split())) + [2])
    board.append([2] * (L + 1))

    # knight info
    knight_info.append(dict())
    for i in range(1, N + 1):
        r, c, h, w, k = map(int, input().split())
        knight_info.append({'y': r, 'x': c, 'h': h, 'w': w, 'k': k, 'scores': 0})
        place_knight_board(i, 4) # 4 is not move

def check_sequential_move(knight_num, direct):
    q = deque()
    visited_knight = [False] * (N + 1)

    visited_knight[knight_num] = True
    q.append(knight_num)

    is_available_move = True

    while q:
        knight_num = q.popleft()

        sel_knight = knight_info[knight_num]

        new_y = sel_knight['y'] + dirs[direct][0]
        new_x = sel_knight['x'] + dirs[direct][1]

        for y in range(new_y, new_y + sel_knight['h']):
            for x in range(new_x, new_x + sel_knight['w']):
                if board[y][x] == 2:
                    is_available_move = False
                    break

                check_knight = knight[y][x]

                if check_knight != 0 and check_knight != knight_num:
                    if not visited_knight[check_knight]:
                        visited_knight[check_knight] = True
                        q.append(check_knight)

            if not is_available_move:
                break
        if not is_available_move:
            break

    return is_available_move, visited_knight

def damage_knight(knight_num):
    sel_knight = knight_info[knight_num]

    score = 0
    for y in range(sel_knight['y'], sel_knight['y'] + sel_knight['h']):
        for x in range(sel_knight['x'], sel_knight['x'] + sel_knight['w']):
            if board[y][x] == 1:
                score += 1

    return score

def commend(knight_num, direction):
    available, visited_knight = check_sequential_move(knight_num, direction)

    if available:
        for i in range(1, N + 1):
            if visited_knight[i]:
                remove_knight_board(i)
        for i in range(1, N + 1):
            if visited_knight[i]:
                place_knight_board(i, direction)

                if i != knight_num:
                    score = damage_knight(i)
                    knight_info[i]['k'] -= score

                    if knight_info[i]['k'] <= 0:
                        remove_knight_board(i)
                    else:
                        knight_info[i]['scores'] += score

def total_score():
    total = 0
    for i in range(1, N + 1):
        if knight_info[i]['k'] <= 0:
            continue
        total += knight_info[i]['scores']

    return total

def solution():
    initialize()

    for _ in range(Q):
        i, d = map(int , input().split())
        if knight_info[i]['k'] <= 0:
            continue

        commend(i, d)

        # print_board(knight)
        # print(knight_info)

    return total_score()


if __name__ == '__main__':
    L, N, Q = map(int, input().split())
    print(solution())
