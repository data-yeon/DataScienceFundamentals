from structures import LinkedList , Stack
from palindrone_prac import isPalindrome

l1 = LinkedList() # 1 -> 2 -> 2 -> 1
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)

# assert 함수가 true 인지아닌지를 확언하겠다.

assert isPalindrome(l1)
assert not isPalindrome(l2)

# 팰린드론인지 확인하는 법
# 모든 요소가 빠질때까지 첫째와 마지막을 뽑아 같은지 비교한다.
def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()


test_stack()