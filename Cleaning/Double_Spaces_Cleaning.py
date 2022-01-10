import pandas as pd
import openpyxl
import xlsxwriter

file_path = 'removed_Characters.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')

# print(df.head(10))
print(df)
for column in df.columns:
    df[column] = df[column].str.replace('\s+' , " ",regex=True)
print(df)
df.to_excel("removed_Double_Spaces.xlsx",engine='xlsxwriter' , index=False , header=True)