arr = [1, 2, 3, 4]
visited = [0] * len(arr)  # visited도 전역으로 둬도 됨


def permutations(n, new_arr):
    global arr
    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0


permutations(2, [])


arr = [1, 2, 3, 4]
def product(n, new_arr):
    global arr
    # 순서 상관 0, 중복 0
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

product(2, [])



arr = [1, 2, 3, 4]

# 현재 인덱스 +1 만큼을 매개변수로 계속 넘겨주어야함
# 순서가 상관없고 중복 불가이기 때문에 현재 인덱스보다 같거나 작은 인덱스는 볼 필요가 없기 때문
def combinations(n, new_arr, c):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)


combinations(2, [], 0)


arr = [1, 2, 3, 4]

def combinations_with_replacement(n, new_arr, c):
    # 순서 상관 X, 중복
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i)


combinations_with_replacement(2, [], 0)