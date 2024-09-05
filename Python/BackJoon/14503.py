N, M = map(int, input().split())

y, x, direction = map(int, input().split())

board = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(N):
    board.append(list(map(int, input().split())))

def dfs(board, y, x, direction, count):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return count
    if board[y][x] == 0 or board[y][x] == 2:
        if board[y][x] == 0:
            count += 1
            board[y][x] = 2

        dir_count = 0
        opposite = 1
        while True:
            direction -= 1
            dir_count += 1
            if direction == -1:
                direction = 3

            if board[y + dy[direction]][x + dx[direction]] == 0:
                break
            if dir_count == 4:
                back_dir = direction + 2
                if back_dir >= 4:
                    back_dir -= 4

                if board[y + dy[back_dir]][x + dx[back_dir]] != 1:
                    opposite = -1
                    break
                else:
                    return count

        ny = y + dy[direction] * opposite
        nx = x + dx[direction] * opposite
        count = dfs(board, ny, nx, direction, count)

    return count


result = dfs(board, y, x, direction, 0)

print(result)