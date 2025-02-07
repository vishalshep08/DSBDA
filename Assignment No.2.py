import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib for visualization
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import zscore

df = pd.read_csv("StudentsPerformance.csv")

#Replacing the null values
#Method 1- Replacing the null values by their respective values
print(df.isnull().sum())
print(df.isnull())

#For the math score column
df['math score'].fillna('NA', inplace=True)
print(df["math score"])

#For the reading score column
# df['reading score'].fillna('NA', inplace=True)
# print(df["reading score"])
df.fillna(df['math score'].mean(), inplace=True)
print(df["math score"])

#For the writing score column
# df['writing score'].fillna('NA', inplace=True)
# print(df["writing score"])
df.fillna('NA', inplace=True)

#printing null values if present
print(df.isnull().sum())
print(df.isnull())

col = ['math score', 'reading score', 'writing score']
#Identification and Handling of Outliers
#Method 1 - BoxPlot
plt.figure(figsize=(10,5))
sns.boxplot(data=df[col])
plt.title("Student Performance")
plt.show()


#Method 2 - Scatterplot
fig, ax = plt.subplots(figsize = (18,10))
ax.scatter(df['math score'], df['reading score'])
ax.set_xlabel('math score')
ax.set_ylabel('reading score')
plt.show()

#Method 3 - Z-Score
df['math score'].fillna('0', inplace=True)
print(df.isnull().sum())
df['math score'] = pd.to_numeric(df['math score'], errors='coerce')
z = np.abs(stats.zscore(df['math score']))
print(z)

#Method 4 - IQR
Q1 = np.percentile(df['math score'],25, interpolation = 'midpoint')
Q3 = np.percentile(df['math score'],75, interpolation = 'midpoint')
IQR = (Q3 - Q1)
print(IQR)

# Above Upper bound
upper = df['math score'] >= (Q3 + 1.5 * IQR)

print("Upper bound:", upper)
print(np.where(upper))

# Below Lower bound
lower = df['math score'] <= (Q1 - 1.5 * IQR)
print("Lower bound:", lower)
print(np.where(lower))

