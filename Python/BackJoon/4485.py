import heapq

INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q,(graph[0][0], 0, 0))
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            return distance[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                ndist = dist + graph[nx][ny]

                if ndist < distance[nx][ny]:
                    distance[nx][ny] = ndist
                    heapq.heappush(q, (ndist, nx, ny))

count = 1

while True:
    n = int(input())
    if n == 0:
        break

    graph =  [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)] 
    answer = dijkstra()

    print('Problem {0}: {1}'.format(count, answer))
    count += 1





