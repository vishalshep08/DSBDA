#Data structures in Pandas
# 1.Series 2.Data frames

import pandas as pd

data = {'Name':['A','B','C','D','E'],'Age':[10,20,30,40,50],'Gender':['Male','Female','Male','Female','Male']}
series = pd.Series(data)
print(series)
print(type(series))


df = pd.DataFrame(data)
print(df)
print(type(df))

print(df['Name'])