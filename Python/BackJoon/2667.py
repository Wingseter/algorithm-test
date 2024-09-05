n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x, y, count):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return count
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        count = dfs(x - 1, y, count)
        count = dfs(x, y - 1, count)
        count = dfs(x + 1, y, count)
        count = dfs(x, y + 1, count)
        return count
    return count

total_danji = 0
house_count = list()
for i in range(n):
    for j in range(n):
        result = dfs(i, j, 0)
        if result != 0:
            total_danji += 1
            house_count.append(result)

house_count.sort()

print(total_danji)
for house in house_count:
    print(house)