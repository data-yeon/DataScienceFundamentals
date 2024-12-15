# def isPalindrome(ln):
#     arr = []
#     head = ln.head
#
#     if not head:
#         return True # head 가 없을 경우, 빈 Linked List.
#
#     node = head
#     # 그러나, head 가 있을 경우에는 노드가 있는동안, 모든 Linked List의 값을 넣는다.
#     while node:
#         arr.append(node.val) # 값을 꺼내서 array에 넣고, 다음요소로 넘어감
#         node = node.next
#
#     while len(arr) > 1:
#         first = arr.pop(0) # 제일 첫번째 거,
#         last = arr.pop() # 제일 마지막 거
#         if first != last:
#             return False
#
#     return True
# def test_problem_stack(s):
#     pair = {
#         '}': '{',
#         ')': '(',
#         ']': '[',
#     }
#     opener = "({["
#     stack = []
#
#     for char in s:
#         if char in opener:
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             top = stack.pop()
#             if pair[char] != top:
#                 return False
#
#     return not stack
# assert test_problem_stack("()")
# assert test_problem_stack("()[]{}")
# assert test_problem_stack("({[][]})")
# assert test_problem_stack("({[]})")
# assert not test_problem_stack("(]")
# assert not test_problem_stack("(()]")
# assert not test_problem_stack("(((])")
# assert not test_problem_stack("((())")