C = int(input())
def countPairings(taken, areFriends):
    first = -1
    for i in range(n):
        if not taken[i]:
            first = i
            break

    if first == -1:
        return 1
    ret = 0
    for pairWith in range(first + 1, n):
        if not taken[pairWith] and areFriends[first][pairWith]:
            # first와 pairWith를 매칭
            taken[first] = taken[pairWith] = True
            # 나머지 학생들에 대해 재귀 호출
            ret += countPairings(taken, areFriends)
            # 매칭 취소 (백트래킹)
            taken[first] = taken[pairWith] = False

    return ret


for i in range(C):
    n, m = map(int, input().split())

    # 2차원 배열을 이용해서 속도 빠르게
    areFriends = [[False] * n for _ in range(n)]
    taken = [False] * n
    friends = list(map(int, input().split()))
    for i in range(m):
        a = friends[i * 2]
        b = friends[i * 2 + 1]
        areFriends[a][b] = True
        areFriends[b][a] = True

    print(countPairings(taken, areFriends))
