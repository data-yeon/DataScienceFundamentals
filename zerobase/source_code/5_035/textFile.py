file = open('C:/pythonTxt/test.txt', 'r')

str = file.read()
print(f'str: {str}')

file.close()




file = open('C:/pythonTxt/about_python.txt', 'r')

str = file.read()
print(f'str: {str}')

file.close()

# str = str.replace('Python', '파이썬')
str = str.replace('Python', '파이썬', 2)
print(f'str: {str}')


file = open('C:/pythonTxt/about_python.txt', 'w')

strCnt = file.write(str)

file.close()
