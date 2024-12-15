# # from inspect import stack
# from structures import LinkedList , Stack
# from palindrone_prac import isPalindrome, test_problem_stack
#
# l1 = LinkedList() # 1 -> 2 -> 2 -> 1
# for num in [1, 2, 2, 1]:
#     l1.append(num)
#
# l2 = LinkedList()
# for num in [1, 2]:
#     l2.append(num)
#
# # assert 함수가 true 인지아닌지를 확언하겠다.
#
# assert isPalindrome(l1)
# assert not isPalindrome(l2)
#
# # 팰린드론인지 확인하는 법
# # 모든 요소가 빠질때까지 첫째와 마지막을 뽑아 같은지 비교한다.
# def test_stack():
#     stack = Stack()
#
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     stack.push(4)
#     stack.push(5)
#
#     assert stack.pop() == 5
#     assert stack.pop() == 4
#     assert stack.pop() == 3
#     assert stack.pop() == 2
#     assert stack.pop() == 1
#     assert stack.pop() is None
#     assert stack.is_empty()
#
#
# # test_stack()
# def test_problem_stack(s):
#     stack = []
#     pair = {
#         ')' : '(',
#         '}': '{',
#         ']' : '[',
#     }
#
#     for char in s:
#         if char in '({[':
#             stack.append(char)
#         else:
#             # 받는게 나왔는데 여는게 비어있으면 이상한것
#             if len(stack) == 0:
#                 return False
#             top = stack.pop() # '{' '}'
#              # 둘이 짝이 안 맞ㄴ는다? :
#             if pair[char] != top: # 여는 괄호가 top과 같은가?
#                 return False
#
#     return len(stack) == 0
#
#     # return True
#     #
#     #
#     # return stack.is_empty()
#
#
#
# # 괄호를 여는 녀석과 닫는 녀석이 구분되어있다.
#
# assert test_problem_stack("()")
# assert test_problem_stack("()[]{}")
# assert test_problem_stack("({[][]})")
# assert test_problem_stack("({[]})")
# assert not test_problem_stack("(]")
# assert not test_problem_stack("(()]")
# assert not test_problem_stack("(((])")
# assert not test_problem_stack("((())")