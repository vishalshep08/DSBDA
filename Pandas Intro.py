#Data structures in Pandas
# 1.Series 2.Data frames

import pandas as pd
import numpy as np

data = {'Name':['A','B','C','D','E'],'Age':[10,20,30,40,50],'Gender':['Male','Female','Male','Female','Male']}
series = pd.Series(data)
print(series)
print(type(series))

df = pd.DataFrame(data)
print(df)
# print(type(df)
# print(df['Name'])

result = df.iloc[1:3, :]
print(result)

result1 = df.loc[1:3, ['Name','Gender']]
print(result1)

df1 = pd.read_csv("D:\\Taleau\\Defence_Export_18102024_0.csv")
print(df1)
print(df1.head)


#Slicing in the series
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)

# Display the Original series
print('Original Series:',s, sep='\n')

# Slice the range of values
result = s[1:3]

# Display the output
print('Values after slicing the Series:', result, sep='\n')

