import maxMod
import modeMod

ages = [25, 27, 27, 24, 31, 34, 33, 31, 29, 25,
        45, 37, 38, 46, 47, 22, 24, 29, 33, 35,
        27, 34, 37, 40, 42, 29, 27, 25, 26, 27,
        31, 31, 32, 38, 25, 27, 28, 40, 41, 34]

print(f'employee cnt: {len(ages)}명')

maxAlg = maxMod.MaxAlgorithm(ages)
maxAlg.setMaxIdxAndNum()
maxAge = maxAlg.getMaxNum()
print(f'maxAge: {maxAge}세')

modAlg = modeMod.ModeAlgorithm(ages, maxAge)
modAlg.setIndexList()
print(f'IndexList: {modAlg.getIndexList()}')

modAlg.printAges()