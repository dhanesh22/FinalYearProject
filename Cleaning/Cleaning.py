import pandas as pd
import openpyxl
import xlsxwriter

file_path = 'Final_Data.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')

# print(df.head(10))

for column in df.columns:
    df[column] = df[column].str.replace(r'\W' , " ",regex=True)
print(df)

df.to_excel("removed_Characters.xlsx",engine='xlsxwriter' , index=False , header=True)