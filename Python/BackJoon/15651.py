n, m = map(int, input().split())
answer = []

def backTracking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+ 1):
        answer.append(i)
        backTracking(depth + 1)
        answer.pop()
backTracking(0)