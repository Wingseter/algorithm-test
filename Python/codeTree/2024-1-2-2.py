'''
문제 정리
먼저 양방향 고려 안함
힙큐 어떻게 쓸지 고민함 lazy delete가 핵심 키 
삭제시 lazy delete에 문제 
힌트 : heap을 매번 돌릴 필요가 없다 
모든 id 가 다르다 
'''
INF = 987654321

import heapq
from collections import Counter

class Graph:
    def __init__(self,n, m, v_n):
        self.n = n
        self.m = m

        self.dest_revenue = [dict() for _ in range(self.n)]
        self.dest_counter = Counter()

        self.id_dict = dict()


        self.starting = 0

        self.dist = []
        self.graph = [[] for _ in range(self.n)]


        for i in range(0, len(v_n), 3):
            start = v_n[i]
            end = v_n[i + 1]
            dist = v_n[i + 2]

            self.graph[start].append([end, dist])
            self.graph[end].append([start, dist])

        self.calculate_dist()

    def new_travel_package(self, id, dest, revenue):
        if revenue not in self.dest_revenue[dest]:
            self.dest_revenue[dest][revenue] = set()

        self.dest_revenue[dest][revenue].add(id)
        self.id_dict[id] = (dest, revenue)
        self.dest_counter[dest] += 1

    def delete_travel_package(self, id):
        if id in self.id_dict:
            dest, revenue = self.id_dict.pop(id)
            self.dest_counter[dest] -= 1
            self.dest_revenue[dest][revenue].remove(id)

    def get_best(self, target_node):
        best_score = -1

        for revenue in self.dest_revenue[target_node].keys():
            if revenue > best_score and len(self.dest_revenue[target_node][revenue]) > 0:
                best_score = revenue

        smallest_id = 987654321
        for ids in self.dest_revenue[target_node][best_score]:
            smallest_id = min(smallest_id, ids)

        return smallest_id, best_score

    def sell_travel_package(self):
        largest_cost = -1
        smallest_id = 987654321

        for target in range(self.n):
            dist_cost = self.dist[target]
            if not self.dest_revenue[target] or dist_cost == INF:
                continue

            if self.dest_counter[target] == 0:
                continue

            find_id, find_rev = self.get_best(target)
            final_cost = find_rev - dist_cost

            if final_cost < 0:
                continue

            if final_cost > largest_cost or final_cost == largest_cost and find_id < smallest_id: # dont care about same id
                smallest_id = find_id
                largest_cost = final_cost

        if smallest_id != INF:
            self.delete_travel_package(smallest_id)
        else:
            smallest_id = -1
        return smallest_id

    def calculate_dist(self):
        # dijkstra
        q = []
        self.dist = [INF] * self.n

        heapq.heappush(q, (0, self.starting))  # 우선순위, 값 형태로 들어간다.
        self.dist[self.starting] = 0 # 자기 자신 있어도 문제 없음

        while q:
            dist, now = heapq.heappop(q)  # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

            if self.dist[now] < dist:  # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
                continue  # 따라서 다음으로 넘어간다.

            for i in self.graph[now]:  # 연결된 모든 노드 탐색
                if dist + i[1] < self.dist[i[0]]:  # 기존에 입력되어있는 값보다 크다면 # 0 = end 1 = dist
                    self.dist[i[0]] = dist + i[1]  #
                    heapq.heappush(q, (dist + i[1], i[0]))
    def new_starting(self, new_starting):
        self.starting = new_starting
        self.calculate_dist()

all_graph = None
def opt_100(n, m, v_n): # create graph
    global all_graph
    all_graph = Graph(n, m, v_n)

def opt_200(id, revenue, dest): # create travel package
    all_graph.new_travel_package(id, dest, revenue) # switch

def opt_300(id): # delete travel package
    all_graph.delete_travel_package(id)

def opt_400(): # sell packages
    answer = all_graph.sell_travel_package()
    return answer

def opt_500(s): # change_start
    all_graph.new_starting(s)

def commender(Q):
    for _ in range(Q):
        commends = list(map(int, input().split()))

        commend = commends[0]

        if commend == 100:
            n = commends[1]
            m = commends[2]
            v_n = commends[3:]
            opt_100(n, m, v_n)

        elif commend == 200:
            id = commends[1]
            revenue = commends[2]
            dest = commends[3]
            opt_200(id, revenue, dest)

        elif commend == 300:
            id = commends[1]
            opt_300(id)

        elif commend == 400:
            answer = opt_400()
            print(answer)

        elif commend == 500:
            s = commends[1]
            opt_500(s)

if __name__ == '__main__':
    Q = int(input())
    commender(Q)