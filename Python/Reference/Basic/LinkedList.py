from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class TreeNode: # 2진 트리
    def __init__(self, val: int = 0,\
                left: Optional['TreeNode'] = None,\
                right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class NTreeNode: # N항 트리
    def __init__(self, val: int = 0, children: Optional[List['TreeNode']] = None):
        self.val = val
        self.children = children if children is not None else []



def traverse(head: ListNode):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

# 연결 리스트 생성
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# 연결 리스트 순회 및 출력
traverse(node1)
