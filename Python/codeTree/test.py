import heapq

# 빈 힙 초기화
a = []

# 원소 추가
heapq.heappush(a, [100, 200])  # 리스트를 추가
heapq.heappush(a, [300, 100])  # 리스트를 추가
heapq.heappush(a, [0, 300])    # 리스트를 추가

print(a)  # 출력: [[0, 300], [300, 100], [100, 200]]
