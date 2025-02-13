dNum = 30

# 10진수 -> X진수
print('2진수: {}'.format(bin(dNum))) # 2진수: 0b11110
print('8진수: {}'.format(oct(dNum))) # 8진수: 0o36
print('16진수: {}'.format(hex(dNum))) # 16진수: 0x1e


print('Type of bin(dNum): {}'.format(type(bin(dNum)))) # Type of bin(dNum): <class 'str'>
print('Type of oct(dNum): {}'.format(type(oct(dNum)))) # Type of oct(dNum): <class 'str'>
print('Type of oct(dNum): {}'.format(type(hex(dNum)))) # Type of oct(dNum): <class 'str'>


# 10진수 -> X진수(format()함수 이용)
print('2진수: {}'.format(format(dNum, '#b'))) # 2진수: 0b11110
print('8진수: {}'.format(format(dNum, '#o'))) # 8진수: 0o36
print('16진수: {}'.format(format(dNum, '#x'))) # 16진수: 0x1e

print('Type of bin(dNum): {}'.format(type(format(dNum, '#b')))) # Type of bin(dNum): <class 'str'>
print('Type of oct(dNum): {}'.format(type(format(dNum, '#o')))) # Type of oct(dNum): <class 'str'>
print('Type of oct(dNum): {}'.format(type(format(dNum, '#x')))) # Type of oct(dNum): <class 'str'>

print('2진수: {0:#b}, 8진수: {0:#o}, 16진수: {0:#x}'.format(dNum, dNum, dNum)) # 2진수: 0b11110, 8진수: 0o36, 16진수: 0x1e
print('2진수: {0:#b}, 8진수: {0:#o}, 16진수: {0:#x}'.format(dNum)) # 2진수: 0b11110, 8진수: 0o36, 16진수: 0x1e

print('2진수: {}'.format(format(dNum, 'b'))) # 2진수: 11110
print('8진수: {}'.format(format(dNum, 'o'))) # 8진수: 36
print('16진수: {}'.format(format(dNum, 'x'))) # 16진수: 1e

print('Type of bin(dNum): {}'.format(type(format(dNum, 'b')))) # Type of bin(dNum): <class 'str'>
print('Type of oct(dNum): {}'.format(type(format(dNum, 'o')))) # Type of oct(dNum): <class 'str'>
print('Type of oct(dNum): {}'.format(type(format(dNum, 'x')))) # Type of oct(dNum): <class 'str'>

print('2진수: {0:b}, 8진수: {0:o}, 16진수: {0:x}'.format(dNum)) # 2진수: 11110, 8진수: 36, 16진수: 1e


# X진수 -> 10진수
print('2진수(0b11110) -> 10진수({})'.format(int('0b11110', 2))) # 2진수(0b11110) -> 10진수(30)
print('8진수(0o36) -> 10진수({})'.format(int('0o36', 8))) # 8진수(0o36) -> 10진수(30)
print('16진수(0x1e) -> 10진수({})'.format(int('0x1e', 16))) # 16진수(0x1e) -> 10진수(30)



# X진수 -> X진수
print('2진수(0b11110) -> 8진수({})'.format(oct(0b11110))) # 2진수(0b11110) -> 8진수(0o36)
print('2진수(0b11110) -> 10진수({})'.format(int(0b11110))) # 2진수(0b11110) -> 10진수(30)
print('2진수(0b11110) -> 16진수({})'.format(hex(0b11110))) # 2진수(0b11110) -> 16진수(0x1e)


print('8진수(0o36) -> 2진수({})'.format(bin(0o36))) # 8진수(0o36) -> 2진수(0b11110)
print('8진수(0o36) -> 10진수({})'.format(int(0o36))) # 8진수(0o36) -> 10진수(30)
print('8진수(0o36) -> 16진수({})'.format(hex(0o36))) # 8진수(0o36) -> 16진수(0x1e)


print('16진수(0x1e) -> 2진수({})'.format(bin(0x1e))) # 16진수(0x1e) -> 2진수(0b11110)
print('16진수(0x1e) -> 8진수({})'.format(oct(0x1e))) # 16진수(0x1e) -> 8진수(0o36)
print('16진수(0x1e) -> 10진수({})'.format(int(0x1e))) # 16진수(0x1e) -> 10진수(30)
