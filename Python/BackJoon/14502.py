from collections import deque

visit1 = [[0 for _ in range(10)] for _ in range(10)]
visit2 = [[0 for _ in range(10)] for _ in range(10)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global answer

    for x in range(n):
        for y in range(m):
            visit1[x][y] = lab[x][y]
            if lab[x][y] == 2:
                queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visit1[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < m and 0 <= nx < n and lab[nx][ny] == 0 and visit1[nx][ny] == 0:
                queue.append((nx, ny))
                visit1[nx][ny] = 1

    cnt = 0
    for x in range(n):
        for y in range(m):
            if lab[x][y] == 0 and visit1[x][y] == 0:
                cnt += 1
    answer = max(answer, cnt)



def back_tracking(select):
    if select == 3:
        bfs()
        return
    for x in range(n):
        for y in range(m):
            if not lab[x][y] and not visit2[x][y]:
                visit2[x][y] = 1
                lab[x][y] = 1
                back_tracking(select + 1)
                lab[x][y] = 0
                visit2[x][y] = 0

queue = deque()
answer = 0
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
back_tracking(0)
print(answer)