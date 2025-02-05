# def sortNumber(ns, asc=True):
#
#     if asc:
#         for i in range(len(ns) - 1):
#             minIdx = i
#
#             for j in range(i + 1, len(ns)):
#                 if ns[minIdx] > ns[j]:
#                     minIdx = j
#
#             ns[i], ns[minIdx] = ns[minIdx], ns[i]
#
#     else:
#         for i in range(len(ns) - 1):
#             maxIdx = i
#
#             for j in range(i + 1, len(ns)):
#                 if ns[maxIdx] < ns[j]:
#                     maxIdx = j
#
#             ns[i], ns[maxIdx] = ns[maxIdx], ns[i]
#
#     return ns


def sortNumber(ns, asc=True):

    cnt = 0

    for i in range(len(ns) - 1):
        targetIdx = i

        for j in range(i + 1, len(ns)):
            if asc:
                if ns[targetIdx] > ns[j]:
                    targetIdx = j
                    cnt += 1
            else:
                if ns[targetIdx] < ns[j]:
                    targetIdx = j
                    cnt += 1

        ns[i], ns[targetIdx] = ns[targetIdx], ns[i]

    print(f'cnt: {cnt}')

    return ns