import pandas as pd
file_path = 'removed_Double_Spaces.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')

for column in df.columns:
    df[column] = df[column].apply(lambda x: x.lower() if type(x) is str else 'empty')
print(df)
df.to_excel("Handled_Empty_Columns.xlsx",engine='xlsxwriter' , index=False , header=True)

