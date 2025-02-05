import bank

koreaBank = bank.Bank()

new_account_name = input('통장 계설을 위한 예금주 입력: ')
myAccount = bank.PrivateBank(koreaBank, new_account_name)
myAccount.printBankInfo()

while True:

    selectNumber = int(input('1.입금, \t2.출금, \t3.종료 '))
    if selectNumber == 1:
        m = int(input('입금액 입력: '))
        koreaBank.doDeposit(myAccount.account_no, m)
        myAccount.printBankInfo()

    elif selectNumber == 2:
        m = int(input('출금액 입력: '))
        try:
            koreaBank.doWithdraw(myAccount.account_no, m)
        except bank.LackException as e:
            print(e)
        finally:
            myAccount.printBankInfo()
    elif selectNumber == 3:
        print('Bye~')
        break

    else:
        print('잘못 입력했습니다. 다시 선택하세요. ')

