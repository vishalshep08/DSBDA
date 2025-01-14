import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 5, 3, 8], 'B': [4, 6, 2, 9]}
df = pd.DataFrame(data)

# Display the input DataFrame
print("Input DataFrame:\n", df)

# Perform binary comparison operations
print("\nLess than 5:\n", df < 5)
print("\nGreater than 5:\n", df > 5)
print("\nLess than or equal to 5:\n", df <= 5)
print("\nGreater than or equal to 5:\n", df >= 5)
print("\nEqual to 5:\n", df == 5)
print("\nNot equal to 5:\n", df != 5)



# Create a Pandas Series
s = pd.Series([10, 20, 30, 40, 50])

# Display the Series
print("Pandas Series:\n", s)

# Perform comparison operations
print("\nLess than 25:\n", s.lt(25))
print("\nGreater than 25:\n", s.gt(25))
print("\nLess than or equal to 30:\n", s.le(30))
print("\nGreater than or equal to 40:\n", s.ge(40))
print("\nNot equal to 30:\n", s.ne(30))
print("\nEqual to 50:\n", s.eq(50))


# Create a DataFrame
data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df)

# Perform comparison operations
print("\nLess than 25:\n", df.lt(25))
print("\nGreater than 50:\n", df.gt(50))
print("\nEqual to 30:\n", df.eq(30))
print("\nLess than or equal to 30:\n", df.le(30))
print("\nGreater than or equal to 40:\n", df.ge(40))
print("\nNot equal to 30:\n", df.ne(30))


# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 0, 3], 'B': [9, 5, 6]})
df2 = pd.DataFrame({'A': [1, 2, 1], 'B': [6, 5, 4]})

# Display the Input DataFrames
print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Perform comparison operations between two DataFrames
print("\nEqual :\n", df1.eq(df2))
print("\nNot Equal:\n", df1.ne(df2))
print("\ndf1 Less than df2:\n", df1.lt(df2))
print("\ndf1 Greater than df2:\n", df1.gt(df2))
print("\ndf1 Less than or equal to df2:\n", df1.le(df2))
print("\ndf1 Greater than or equal to df2:\n", df1.ge(df2))