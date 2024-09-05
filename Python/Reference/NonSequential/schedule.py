def findItinerary_recursive(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets, reverse = True):
        graph[a].append(b)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]

def findItinerary_loop(self, tickets: List[List[str]]) -> List[str]:
    import collections
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets, reverse = True):
        graph[a].append(b)

    route, stack = [], ['JFK']

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]