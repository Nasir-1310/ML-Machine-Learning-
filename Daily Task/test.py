import pandas as pd

data = pd.read_excel("data.xlsx")
print("📄 Columns in your Excel file:")
print(data.columns)
