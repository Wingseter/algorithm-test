def min_average_subarray(arr, N, M):
    # 누적합 배열 생성 (prefix_sum[i] = arr[0]부터 arr[i-1]까지의 합)
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    # 최소 평균을 저장할 변수
    min_avg = float('inf')

    # 슬라이딩 윈도우로 M개 이상의 연속된 요소의 평균 구하기
    for i in range(N - M + 1):  # 윈도우의 시작점
        for j in range(i + M, N + 1):  # 윈도우의 끝점, 최소 M개의 길이
            # 부분 배열의 합: prefix_sum[j] - prefix_sum[i]
            total_sum = prefix_sum[j] - prefix_sum[i]
            length = j - i
            avg = total_sum / length
            min_avg = min(min_avg, avg)

    return min_avg

# 예시 배열
arr = [1, 2, 3, 1, 2, 3]
N = len(arr)
M = 3

# 결과 출력
result = min_average_subarray(arr, N, M)
print(f"최소 평균 값: {result:.5f}")
