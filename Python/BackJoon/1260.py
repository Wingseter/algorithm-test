from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for index in graph:
    index.sort()

visit_dfs = []
def dfs(node):
    visit_dfs.append(node)
    if len(graph[node]) == 0:
        return
    else:
        for connected in graph[node]:
            if connected in visit_dfs:
                continue
            dfs(connected)

visit_bfs = []
def bfs(start):
    Q = deque()
    Q.append(start)
    visit_bfs.append(start)

    while Q:
        node = Q.popleft()
        for connected in graph[node]:
            if connected in visit_bfs:
                continue
            Q.append(connected)
            visit_bfs.append(connected)
dfs(v)
bfs(v)
print(' '.join(map(str, visit_dfs)))
print(' '.join(map(str, visit_bfs)))