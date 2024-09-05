import collections

N, M = map(int , input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

visited = [[0]*M for _ in range(N)]

def bfs(sy, sx):
    Q = collections.deque()
    Q.append((sy, sx))
    visited[sy][sx] = 1

    while Q:
        y, x = Q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny <= -1 or nx <= -1 or ny >= N or nx >= M:
                continue
            if board[ny][nx] == 0:
                continue

            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                Q.append((ny, nx))
    return visited[N- 1][M-1]

print(bfs(0, 0))


