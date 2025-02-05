file = open('C:/pythonTxt/test.txt', 'w')

strCnt = file.write('Hello world~')
print(f'strCnt: {strCnt}')

file.close()


file = open('C:/pythonTxt/test.txt', 'w')

strCnt = file.write('Hello python~')
print(f'strCnt: {strCnt}')

file.close()


import time

lt = time.localtime()
dateStr = '[' + str(lt.tm_year) + '년 ' + \
          str(lt.tm_mon) + '월 ' +\
          str(lt.tm_mday) + '일] '

todaySchedule = input('오늘 일정: ')

file = open('C:/pythonTxt/test.txt', 'w')
file.write(dateStr + todaySchedule)
file.close()



import time

lt = time.localtime()
# dateStr = time.strftime('%Y-%m-%d %H:%M:%S %p', lt)
dateStr = '[' + time.strftime('%Y-%m-%d %I:%M:%S %p', lt) + '] '

todaySchedule = input('오늘 일정: ')

file = open('C:/pythonTxt/test.txt', 'w')
file.write(dateStr + todaySchedule)
file.close()

