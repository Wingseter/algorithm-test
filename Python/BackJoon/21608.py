import math
N = int(input())

cls_list = [[0] * N for _ in range(N)]
filt_list = []

four_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
score = 0

def seat(people, friends):
    global score
    best_choice = {'pos_x': 0, 'pos_y': 0, 'empty': -1, 'favor': 0}
    for y in range(N):
        for x in range(N):
            if cls_list[y][x] != 0:
                continue
            favorite = 0
            empty_seat = 0

            for direction in four_dir:
                nx = x + direction[0]
                ny = y + direction[1]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                elif cls_list[ny][nx] != 0:  # 사람 있어
                    for friend in friends:
                        if cls_list[ny][nx] == friend:
                            favorite += 1
                else:  # 빈자리
                    empty_seat += 1

            if favorite > best_choice['favor']:
                best_choice['pos_x'] = x
                best_choice['pos_y'] = y
                best_choice['favor'] = favorite
                best_choice['empty'] = empty_seat
            elif favorite == best_choice['favor'] and empty_seat > best_choice['empty']:
                best_choice['pos_x'] = x
                best_choice['pos_y'] = y
                best_choice['favor'] = favorite
                best_choice['empty'] = empty_seat
            elif best_choice['favor'] == 0 and empty_seat > best_choice['empty']:
                best_choice['pos_x'] = x
                best_choice['pos_y'] = y
                best_choice['empty'] = empty_seat

    cls_list[best_choice['pos_y']][best_choice['pos_x']] = people

def culc_score

for _ in range(N * N):
    input_list = list(map(int, input().split()))
    target = input_list[0]
    friend = input_list[1:]
    seat(target, friend)

print(score)
