import copy # 깊은 복사를 사용하기 위한 모듈,

def bubbleSort(ns, deepCopy = True):
    # 깊은 복사를 하기위해서 이렇게 만듦.

    # 깊은 복사를 사용해, 새로운 레퍼런스를 만들고 싶다면.
    if deepCopy:
        # 새로운 녀석을 카피해서 .
        cns = copy.copy(ns)
    else:
        cns = ns # 이러면 얕은 복사임.

    length = len(cns) - 1
    for i in range(length):
        for j in range(length - i):
            if cns[j] > cns[j + 1]:
                cns[j], cns[j + 1] = cns[j + 1], cns[j]

    return cns

