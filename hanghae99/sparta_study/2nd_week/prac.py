from collections import deque


def isPalindrome(ln):
    arr = []
    head = ln.head

    if not head:
        return True # head 가 없을 경우, 빈 Linked List.

    node = head
    # 그러나, head 가 있을 경우에는 노드가 있는동안, 모든 Linked List의 값을 넣는다.
    while node:
        arr.append(node.val) # 값을 꺼내서 array에 넣고, 다음요소로 넘어감
        node = node.next

    while len(arr) > 1:
        first = arr.pop(0) # 제일 첫번째 거,
        last = arr.pop() # 제일 마지막 거
        if first != last:
            return False

    return True
def test_problem_stack(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack

def test_problem_queue(num):
    # deq = deque([i for i in range(1, num + 1)])
    # while len(deq) > 1:
    #     deq.popleft()
    #     deq.append(deq.popleft())
    # return deq.popleft()
    # deq = deque([1,2,3])
    # deq.append()
    # deq.appendleft()
    # deq.pop()
    # deq.popleft() # 양쪽으로 쓸 수 있고, 빠르다.
    deq = deque([i for i in range(1, num + 1)])  # [1,2,3,4,5,6]
    while len(deq) > 1:
        deq.popleft()
        front = deq.popleft()
        deq.append(front) # 이걸 deq에 남는게 하나일 때 까지 계속 반복

