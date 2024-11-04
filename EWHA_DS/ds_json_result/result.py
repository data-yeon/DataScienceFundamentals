import json

# JSON 파일 불러오기
with open('/EWHA_DS/ds_json_result/json/result_re.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# 예외 카운트 초기화
exception_count_1 = 0  # 0~349번째에서 "$N-output"이 1이 아닌 경우
exception_count_0 = 0  # 350~699번째에서 "$N-output"이 0이 아닌 경우
# 조건에 따라 예외 확인
for i, item in enumerate(data):
    output_value = item.get("$N-output")
    if 0 <= i < 350:  # 0~349번째 인덱스
        if output_value != 1:
            exception_count_1 += 1
    elif 350 <= i < 700:  # 350~699번째 인덱스
        if output_value != 0:
            exception_count_0 += 1
# 결과 출력
print(f"0~349번째에서 1이 아닌 값의 예외 갯수: {exception_count_1}")
print(f"350~699번째에서 0이 아닌 값의 예외 갯수: {exception_count_0}")