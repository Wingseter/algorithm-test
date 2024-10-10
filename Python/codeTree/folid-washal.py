# 플로이드-워셜 알고리즘
n, m = map(int, input().split())  # 노드 개수, 간선 개수
INF = float('inf')

# 인접 행렬 초기화 (무한대 값으로)
dist = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 거리는 0으로 설정
for i in range(1, n + 1):
    dist[i][i] = 0

# 간선 입력 받기
for _ in range(m):
    u, v, w = map(int, input().split())  # u -> v 의 비용 w
    dist[u][v] = w  # 간선 정보 저장

# 플로이드-워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 최단 거리 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
