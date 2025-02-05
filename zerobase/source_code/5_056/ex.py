import ADictionary as dic

kTe = dic.KorToEng()

# 단어 등록
kTe.registWord('책', 'bok')
kTe.registWord('나비', 'butterfly')
kTe.registWord('연필', 'pencil')
kTe.registWord('학생', 'studen')
kTe.registWord('선생님', 'teacher')

# 단어 수정
kTe.updateWord('책', 'book')
kTe.updateWord('학생', 'student')

# 단어 검색
print(f'책 : {kTe.searchWord("책")}')
print(f'나비 : {kTe.searchWord("나비")}')
print(f'연필 : {kTe.searchWord("연필")}')
print(f'학생 : {kTe.searchWord("학생")}')
print(f'선생님 : {kTe.searchWord("선생님")}')

# 단어 삭제
kTe.removeWord('책')

# 사전 출력
kTe.printWords()


kTj = dic.KorToJpa()

# 단어 등록
kTj.registWord('책', '本')
kTj.registWord('나비', '蝶')
kTj.registWord('연필', '鉛筆')
kTj.registWord('학생', '学生')
kTj.registWord('선생님', '先生')

# 단어 수정
kTj.updateWord('책', '蝶')
kTj.updateWord('학생', '学生')

# 단어 검색
print(f'책 : {kTj.searchWord("책")}')
print(f'나비 : {kTj.searchWord("나비")}')
print(f'연필 : {kTj.searchWord("연필")}')
print(f'학생 : {kTj.searchWord("학생")}')
print(f'선생님 : {kTj.searchWord("선생님")}')

# 단어 삭제
kTj.removeWord('책')

# 사전 출력
kTj.printWords()