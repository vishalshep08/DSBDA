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