from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(maps):
    q = deque()
    q.append((0, 0))

    visited = [[-1] * 5 for _ in range(5)]
    visited[0][0] = 1

    while q:
        y, x = q.popleft()

        if y == 4 and x == 4:
            return visited[y][x]  # 도착점까지의 거리 반환

        for my, mx in dirs:
            ny = y + my
            nx = x + mx


            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue

            if maps[ny][nx] != 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

    return -1


def solution(maps):
    answer = 0

    answer = bfs(maps)

    return answer