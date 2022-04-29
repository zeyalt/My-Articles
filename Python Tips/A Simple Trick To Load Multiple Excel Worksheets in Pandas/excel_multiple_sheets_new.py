import pandas as pd

# Define filepath
filepath = 'data/sales.xlsx'

# Load file with `sheet_name=None` - returns a dictionary
df_dict = pd.read_excel(filepath, sheet_name=None)

# Combine data from all worksheets as single DataFrame
df_all = pd.concat(df_dict.values(), ignore_index=True)