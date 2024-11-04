def length_of_longest_substring(s):
    char_index = {}  # 각 문자의 위치를 저장할 해시테이블 (딕셔너리)
    start = 0  # 부분 문자열의 시작 위치
    max_length = 0  # 가장 긴 부분 문자열의 길이

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # 중복 문자가 있으면 시작 위치를 갱신

        char_index[char] = i  # 현재 문자의 위치 저장
        max_length = max(max_length, i - start + 1)  # 현재 부분 문자열의 길이와 최대 길이 비교

    return max_length