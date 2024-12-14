from operator import index

import  pandas as pd

df = pd.read_csv('coffee.csv')
print(df.head())

df2 =  df.rename(index= {0: 'a', 1: 'b', 2: 'c' })
print(df2.head())