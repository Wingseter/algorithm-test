def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1:  # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i + 1:], r - 1):
                yield [array[i]] + next


for i in combinations_2([1, 2, 3, 4], 3):
    print(i, end=" ")

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combination(array[i + 1:], r - 1):
                yield [array[i]] + next