import collections

shark_y, shark_x  = 0,0
shark_size = 2
eat_cnt = 0
fish_cnt = 0
time = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if 0 < board[y][x] <= 6:
            fish_cnt +=1
        elif board[y][x] == 9:
            shark_y, shark_x = y, x

board[shark_y][shark_x]=0

def bfs(shark_y, shark_x):
    q = collections.deque([(shark_y, shark_x, 0)])
    dist_list = []
    visited = [[False] * N for _ in range(N)]
    visited[shark_y][shark_x] = True
    min_dist = 987654321
    while q:
        y, x, dist = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if board[ny][nx] <= shark_size:
                    visited[ny][nx] = True
                    if 0 < board[ny][nx] < shark_size:
                        min_dist = dist
                        dist_list.append((dist + 1, ny, nx))
                    if dist + 1 <= min_dist:
                        q.append((ny, nx, dist + 1))

    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False

while fish_cnt:
    result = bfs(shark_y, shark_x)
    if not result:
        break
    shark_y, shark_x = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1
    if shark_size == eat_cnt:
        shark_size += 1
        eat_cnt = 0

    board[shark_y][shark_x] = 0

print(time)