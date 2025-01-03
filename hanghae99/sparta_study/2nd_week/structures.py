class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)

class Node:
    def __init__(self, val = 0, next= None):
        self.val = val # Node의 값
        self.next = next # 다음 노드를 가리키는 포인터.

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if not self.top: # self의 top이 none라는 뜻.
            return None
        node = self.top
        self.top = self.top.next # 기존의 top은 node의 next가 되어야 함.
        return node.val

    def is_empty(self):
        return self.top is None

class Queue:
    # def __init__(self):
    #     self.front = None
    #
    # def push(self, value):
    #     if not self.front:
    #         self.front = Node(value)
    #         return
    #
    #     node = self.front
    #     while node.next:
    #         node = node.next
    #     node.next = Node(value)
    #
    # def pop(self):
    #     if not self.front:
    #         return None
    #
    #     node = self.front
    #     self.front = self.front.next
    #     return node.val
    #
    # def is_empty(self):
    #     return self.front is None

    # push, pop , is_empty 가 필요 .
    def __init__(self):
        self.front = None

    def push(self, val):
        # 큐에 값을 추가
        # linked list 에서 만들었던, node 활용
        if self.front is None: # if not self.front: # 큐가 비어있으면, 첫번째 노드 설정
            self.front = Node(val)
            return
        node = self.front
        while node.next:  # node의 next가 있는 동안 (마지막 노드까지 이동)
            node = node.next
        node.next = Node(val) # 마지막 노드의 next를  새 노드로 연결
    def pop(self):
        # 큐에서 값을 제거 후 반환
        if not self.front: # 큐가 비어있으면 None반환
            return None

        node = self.front # 맨 앞 노드를 저장
        self.front = node.next # self의 front를 node의 next로 한다.
        return node.val # 기존의 제일 앞에 있던 값을 돌려주기
    def is_empty(self):
        return self.front is None
        # pass

