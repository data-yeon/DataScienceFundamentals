def exampleResult(s1, s2, s3, s4, s5):

    passAvgScore = 60
    limitScore = 40

    def getTotal():
        totalScore = s1 + s2 + s3 + s4 + s5
        print(f'총점: {totalScore}')
        return totalScore

    def getAverage():
        avg = getTotal() / 5
        print(f'평균: {avg}')
        return avg

    def printPassOrFail():
        print(f'{s1}: Pass') if s1 >= limitScore else print(f'{s1}: Fail')
        print(f'{s2}: Pass') if s2 >= limitScore else print(f'{s2}: Fail')
        print(f'{s3}: Pass') if s3 >= limitScore else print(f'{s3}: Fail')
        print(f'{s4}: Pass') if s4 >= limitScore else print(f'{s4}: Fail')
        print(f'{s5}: Pass') if s5 >= limitScore else print(f'{s5}: Fail')

    def printFinalPassOrFail():

        if getAverage() >= passAvgScore:
            if s1 >= limitScore and s2 >= limitScore and s3 >= limitScore and s4 >= limitScore and s5 >= limitScore:
                print('Final Pass!!')

            else:
                print('Final Fail!!')

        else:
            print('Final Fail!!')


    getAverage()
    printPassOrFail()
    printFinalPassOrFail()



if __name__ == '__main__':
    sub1 = int(input('과목1 점수 입력: '))
    sub2 = int(input('과목2 점수 입력: '))
    sub3 = int(input('과목3 점수 입력: '))
    sub4 = int(input('과목4 점수 입력: '))
    sub5 = int(input('과목5 점수 입력: '))

    exampleResult(sub1, sub2, sub3, sub4, sub5)







def exampleResult(*s):

    passAvgScore = 60
    limitScore = 40

    def getTotal():
        totalScore = sum(s)
        print(f'총점: {totalScore}')
        return totalScore

    def getAverage():
        avg = getTotal() / len(s)
        print(f'평균: {avg}')
        return avg

    def printPassOrFail():
        for idx, score in enumerate(s):
            print(f'과목{idx+1}: Pass') if score >= limitScore else print(f'과목{idx+1}: Fail')

    def printFinalPassOrFail():

        result = 'Final Pass!!'

        if getAverage() >= passAvgScore:
            for idx, score in enumerate(s):
                if score < limitScore:
                    result = 'Final Fail!!'
                    break
        else:
            result = 'Final Fail!!'

        print(result)

    getAverage()
    printPassOrFail()
    printFinalPassOrFail()





if __name__ == '__main__':
    sub1 = int(input('과목1 점수 입력: '))
    sub2 = int(input('과목2 점수 입력: '))
    sub3 = int(input('과목3 점수 입력: '))
    sub4 = int(input('과목4 점수 입력: '))
    sub5 = int(input('과목5 점수 입력: '))
    exampleResult(sub1, sub2, sub3, sub4, sub5)
