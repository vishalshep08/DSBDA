import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

print("Original DataFrame:\n", unsorted_df)

# Sort the DataFrame by labels
sorted_df=unsorted_df.sort_index()
print("\nOutput Sorted DataFrame:\n", sorted_df)