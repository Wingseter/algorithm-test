from collections import deque

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int , input())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs():
    start_y, start_x = 0, 0
    Q = deque()
    Q.append((start_y, start_x))

    while Q:
        y, x = Q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny <= -1 or ny >= N or nx <= -1 or nx >= M:
                continue

            if board[ny][nx] == 0:
                continue

            if board[ny][nx] == 1:
                board[ny][nx] = board[y][x] + 1
                Q.append((ny, nx))

    return board[N - 1][M - 1]


print(bfs())
