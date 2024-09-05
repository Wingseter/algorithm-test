from collections import deque
M, N, H = map(int, input().split())

graph = []
for _ in range(H):
    flore = []
    for _ in range(N):
        tomatos = list(map(int, input().split()))
        flore.append(tomatos)
    graph.append(flore)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs_3d(z, y, x):
    queue = deque()
    queue.append((z, y, x))

    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H:
                continue
            if graph[nz][ny][nx] == -1:
                continue
            if graph[nz][ny][nx] == 0 or graph[z][y][x] + 1 < graph[nz][ny][nx]:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))

# 완전탐색
for x in range(M):
    for y in range(N):
        for z in range(H):
            if graph[z][y][x] == 1:
                bfs_3d(z, y, x)

answer = 0
for x in range(M):
    for y in range(N):
        for z in range(H):
            if graph[z][y][x] == 0:
                answer = -1
if answer == -1:
    print(answer)
else:
    max = -1
    for x in range(M):
        for y in range(N):
            for z in range(H):
                if graph[z][y][x] > max:
                    max = graph[z][y][x]
    print(max - 1)

