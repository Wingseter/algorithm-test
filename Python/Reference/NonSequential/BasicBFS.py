graph = list()

def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered

from collections import deque

def degue_bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[i]:
            queue.append(i)
            visited[i] = True
graph = list()
visited = [False] * 9
degue_bfs(graph, 1, visited)