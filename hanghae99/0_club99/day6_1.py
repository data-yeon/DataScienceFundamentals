def should_ring_bell(repeat_num, cards):
    betting_table = {}

    # 카드 정보를 누적
    for kind, value in cards:
        if kind in betting_table:
            betting_table[kind] += value
        else:
            betting_table[kind] = value

    # 과일 종류 중 개수가 정확히 5개인 경우가 있는지 확인
    for count in betting_table.values():
        if count == 5:
            return "YES"

    return "NO"


# 예제 입력
repeat_num = 3
cards = [
    ("STRAWBERRY", 2),
    ("BANANA", 3),
    ("LIME", 5)
]

# 함수 호출 및 결과 출력
print(should_ring_bell(repeat_num, cards))  # 출력: YES