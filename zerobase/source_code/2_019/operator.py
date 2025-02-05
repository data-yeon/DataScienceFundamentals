cha1 = 'A'      # 65
cha2 = 'S'      # 83

print('\'{}\' > \'{}\' : {}'.format(cha1, cha2, (cha1 > cha2)))
print('\'{}\' >= \'{}\' : {}'.format(cha1, cha2, (cha1 >= cha2)))
print('\'{}\' < \'{}\' : {}'.format(cha1, cha2, (cha1 < cha2)))
print('\'{}\' <= \'{}\' : {}'.format(cha1, cha2, (cha1 <= cha2)))
print('\'{}\' == \'{}\' : {}'.format(cha1, cha2, (cha1 == cha2)))
print('\'{}\' != \'{}\' : {}'.format(cha1, cha2, (cha1 != cha2)))

print('\'A\' -> {}'.format(ord('A')))
print('\'S\' -> {}'.format(ord('S')))

print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))


str1 = 'Hello'
str2 = 'hello'

print('{} == {} : {}'.format(str1, str2, (str1 == str2)))
print('{} != {} : {}'.format(str1, str2, (str1 != str2)))


userInputAlphabet = input('알파벳 입력 : ')
print('{} : {}'.format(userInputAlphabet, ord(userInputAlphabet)))

userInputASCII = int(input('아스키 코드 입력 : '))
print('{} : {}'.format(userInputASCII, chr(userInputASCII)))

# print(chr(104))

# systemID = 'administrator@gmail.com'
# sysoutPW = '!@#$%qwertyQWERTY'
#
# userInputId = input('아이디 입력 : ')
# userInputPw = input('비번 입력 : ')
#
# print('아이디 비교 결과 : {}'.format(systemID == userInputId))
# print('비번 비교 결과 : {}'.format(sysoutPW == userInputPw))