n, m = map(int, input().split())
answer = []


def backtraking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n + 1):
        if i in answer:
            continue
        answer.append(i)
        backtraking(depth + 1)
        answer.pop()


backtraking(0)
