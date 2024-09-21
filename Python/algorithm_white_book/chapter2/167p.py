n = 0
MAX = 10
dist = [[None] * MAX for _ in range(MAX)]

visited = [False] * MAX

def shortestPath(path, visited, currentLength):
    if len(path) == n:
        return currentLength + dist[path[0][path[-1]]]

    ret = 987654321

    for next in n:
        if visited[next]:
            continue
        here = path[-1]
        path.append(next)
        visited[next] = True

        card = shortestPath(path, visited, currentLength + dist[here][next])
        ret = min(ret, card)
        visited[next] = False
        path.pop()

    return ret

