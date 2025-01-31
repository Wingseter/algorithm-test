def illuminate(board, x, y, obstacles):
    N = len(board)
    left_bound, right_bound = y, y  # 빛이 확산되는 좌우 경계

    for i in range(N):
        row = x + i  # 아래로 한 줄씩 내려감
        if row >= N:
            break  # 보드를 벗어나면 중단

        for j in range(left_bound, right_bound + 1):
            if j < 0 or j >= N:
                continue  # 보드를 벗어나면 무시
            if (row, j) in obstacles:  # 장애물을 만나면
                if j <= y:  # 장애물이 왼쪽에 있으면 left_bound 갱신
                    left_bound = j + 1
                else:  # 장애물이 오른쪽에 있으면 right_bound 갱신
                    right_bound = j - 1
                continue
            board[row][j] = 1  # 빛을 퍼뜨림

        # 좌우로 한 칸씩 확장
        left_bound = max(0, left_bound - 1)
        right_bound = min(N - 1, right_bound + 1)

    # 출력
    for row in board:
        print(row)


# N x N 보드 크기
N = 6
# 빈 보드
board = [[0] * N for _ in range(N)]

# 빛의 시작 위치
start_x, start_y = 3, 1

# 장애물 위치
obstacles = {(2, 5), (4, 2)}

# 빛 퍼뜨리기
illuminate(board, start_x, start_y, obstacles)
