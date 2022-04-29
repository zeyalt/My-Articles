import pandas as pd

# Define filepath
filepath = 'data/sales.xlsx'

# Load Excel file using Pandas
f = pd.ExcelFile(filepath)

# Define an empty list to store individual DataFrames
list_of_dfs = []

# Iterate through each worksheet
for sheet in f.sheet_names:
    
    # Parse data from each worksheet as a Pandas DataFrame
    df = f.parse(sheet)

    # And append it to the list
    list_of_dfs.append(df)
    
# Combine all DataFrames into one
data = pd.concat(list_of_dfs, ignore_index=True)

# Preview first 10 rows
data.head(10)