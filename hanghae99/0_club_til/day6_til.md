# 할리갈리 게임에서 종을 쳐야 하는지 판단하는 코드
![hanghae Logo](https://hanghae99.spartacodingclub.kr/_next/image?url=https%3A%2F%2Fstatic.spartacodingclub.kr%2Fhanghae99%2F99club%2Fproblems%2Fcoding-test-til.png&w=640&q=75)
#### [백준링크](https://www.acmicpc.net/problem/27160)


```python
import sys
input = sys.stdin.readline

n = int(input()) # 첫 번째 입력 줄에서 카드 개수 n을 입력받아 정수형으로 변환

dic = {}  # dic이라는 빈 딕셔너리를 초기화하여, 각 과일 종류의 개수를 저장할 공간을 만듭니다. 딕셔너리의 키는 과일 이름, 값은 과일의 개수를 의미합니다.

for i in range(n) :  # 카드 개수 n만큼 반복하여 각 카드 정보를 입력받기 
    word, number = input().split() # input().split()으로 과일 이름(word)과 개수(number)를 공백 기준으로 분리하여 각각 저장합니다.
    if word in dic.keys() : # 조건을 통해 딕셔너리에 word(과일 이름)가 이미 존재하는지 확인합니다.
        dic[word] += int(number) 
    else :
        dic[word] = int(number)

for key in dic.keys() :
    if dic[key] == 5 :
        print('YES')
        break
else :
    print('NO')
```
