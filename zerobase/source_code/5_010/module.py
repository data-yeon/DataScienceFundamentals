import calculator

calculator.add(20, 10)
calculator.sub(20, 10)
calculator.mul(20, 10)
calculator.div(20, 10)


import lottoMachine

lottoNumbers = lottoMachine.getLottoNumbers()
print(f'lottoNumbers: {lottoNumbers}')


import reverseStr

userInputStr = input('문자열 입력: ')
reversedString = reverseStr.reverseStr(userInputStr)
print(f'reversedString: {reversedString}')