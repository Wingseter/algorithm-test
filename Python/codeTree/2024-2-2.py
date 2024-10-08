'''
되돌아 볼 점

새로운 트리를 생성하는 것에서 시간을 낭비했다 문제를 제대로 읽자
비트 연산을 사용할 바에 차라리 배열을 써버리자 그게 더 실수가 없다
문제를 제대로 읽지 않았다. 색상을 바꾸는 것에서 서브 노드 전부 했어야 했다. 따라서 서브 노드도 저장해야 한다.
'''

class TreeNode:
    def __init__(self, m_id, color, max_depth):
        self.m_id = m_id
        self.color = color
        self.sub_node = []
        self.max_depth = max_depth

class Tree:
    def __init__(self):
        self.node_map = {}

    def insert(self, m_id, p_id, color, max_depth):
        new_node = TreeNode(m_id, color, max_depth)

        if p_id == -1: # add to root node
            self.node_map[m_id] = [new_node, p_id]

        else: # add to sub node
            available_depth = 2
            available_insert = True

            # check node can add
            parent_id = p_id
            while parent_id != -1:
                parent_node = self.node_map[parent_id][0]
                if parent_node.max_depth < available_depth: # cant add node
                    available_insert = False
                    break
                available_depth += 1
                parent_id = self.node_map[parent_id][1]

            if available_insert:
                self.node_map[p_id][0].sub_node.append(m_id)
                self.node_map[m_id] = [new_node, p_id]
    def change_color(self, m_id, color):
        self.node_map[m_id][0].color = color

        if len(self.node_map[m_id][0].sub_node) == 0:
            return
        else:
            for sub_id in self.node_map[m_id][0].sub_node:
                self.change_color(sub_id, color)

    def search_color(self, m_id):
        return self.node_map[m_id][0].color

    def calculate_score(self):
        memo = dict()
        final_score = 0
        for roll_id in self.node_map.keys():
            search_m_id = roll_id
            node_color = self.node_map[search_m_id][0].color

            # parent circulate
            while search_m_id != -1:

                if search_m_id not in memo:
                    memo[search_m_id] = [0, 0, 0, 0, 0]

                memo[search_m_id][node_color - 1] = 1

                search_m_id = self.node_map[search_m_id][1] # parent_node

        for mem_val in memo.values():
            count_one = mem_val.count(1)
            final_score += count_one **2

        return final_score

super_tree = Tree()

def opt_100(m_id, p_id, color, max_depth):
    super_tree.insert(m_id, p_id, color, max_depth)

def opt_200(m_id, color):
    super_tree.change_color(m_id, color)

def opt_300(m_id):
    result = super_tree.search_color(m_id)
    print(result)

def opt_400():
    result = super_tree.calculate_score()
    print(result)

def commender():
    commend = list(map(int, input().split()))

    option = commend[0]

    if option == 100: # add node
        m_id, p_id, color, max_depth = commend[1:5]
        opt_100(m_id, p_id, color, max_depth)
    elif option == 200: # change color
        m_id, color = commend[1:3]
        opt_200(m_id, color)
    elif option == 300: # search color
        m_id = commend[1]
        opt_300(m_id)
    elif option == 400: # calc
        opt_400()

if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        commender()