import sys
sys.stdin = open('sample_input.txt', "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    names = set()

    for count in range(N):
        names.add(input())

    result = sorted(names)

    print(f"#{test_case}")
    for name in result:
        print(name)
        