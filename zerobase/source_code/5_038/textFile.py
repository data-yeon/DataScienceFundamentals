languages = ['c/c++', 'java', 'c#', 'python', 'javascript']

uri = 'C:/pythonTxt/'
for item in languages:
    with open(uri + 'languages.txt', 'a') as f:
        f.write(item)
        f.write('\n')




languages = ('c/c++', 'java', 'c#', 'python', 'javascript')

uri = 'C:/pythonTxt/'
with open(uri + 'languages.txt', 'a') as f:
    # f.writelines(languages)
    f.writelines(item + '\n' for item in languages)




scoreDic = {'kor': 85, 'eng': 90, 'mat': 92, 'sci': 79, 'his': 82}

uri = 'C:/pythonTxt/'
for key in scoreDic.keys():
    with open(uri + 'scoreDic.txt', 'a') as f:
        f.write(key + '\t: ' + str(scoreDic[key]) + '\n')



dic = {'s1':90, 's2':85, 's3': 95}
list = [90, 85, 95]

uri = 'C:/pythonTxt/'
with open(uri + 'scores.txt', 'a') as f:
    print(dic, file=f)





