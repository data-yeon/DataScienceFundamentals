def divisor(inputNumber):
    result = []
    for number in range(1, (inputNumber + 1)):
        if inputNumber % number == 0:
            result.append(number)

    return result



def prime_number(inputNumber):
    result = []
    for number in range(2, (inputNumber + 1)):
        flag = True
        for n in range(2, number):
            if number % n == 0:
                flag = False
                break

        if (flag):
            result.append(number)

    return result