

from structures import LinkedList, Stack
from palindrone_prac import isPalindrome

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)


    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.val

    def is_empty(self):
        return self.top is None

# class Node:
#     def __init__(self, val=0, next=None):
#         # 상자에 들어갈 값과 다음에 뭘 가르킬지 화살표
#         self.val = val
#         self.next = next
#
