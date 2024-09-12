def all_friend_available(n, friends, matched):
    # 모든 학생이 짝이 지어진 경우 경우의 수를 1로 반환
    # 오답노트: 무조건 정답을 반환할 필요 없다 1을 반환해서 카운트에 추가하자
    if all(matched):
        return 1

    # 매칭되지 않은 첫 번째 학생 찾기
    first = -1
    for i in range(n):
        if not matched[i]:
            first = i
            break

    count = 0
    # 첫 번째 학생과 매칭할 친구 찾기
    for j in range(first + 1, n):
        if not matched[j] and (first, j) in friends:
            # 두 학생을 매칭 처리
            # 매칭 배열을 만드는것이 좋았다
            matched[first] = matched[j] = True
            # 나머지 학생들에 대해 재귀 호출
            count += all_friend_available(n, friends, matched)
            # 매칭 취소 (백트래킹)
            matched[first] = matched[j] = False

    return count


C = int(input())  # Test Case

for _ in range(C):
    n, m = map(int, input().split())
    friend_input = list(map(int, input().split()))

    friends = []
    for i in range(m):
        a = friend_input[2 * i]  # 학생 번호를 0부터 시작하도록 맞추기
        b = friend_input[2 * i + 1]
        friends.append((a, b))
        friends.append((b, a))  # 양방향 친구 추가

    matched = [False] * n
    result = all_friend_available(n, friends, matched)
    print(result)
