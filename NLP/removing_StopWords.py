import pandas as pd
import nltk
from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('stopwords')


file_path = 'Handled_Empty_Columns.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')
print(df.head(20))

stop_words= set(stopwords.words('english'))
for column in df.columns:
    df[column] = df[column].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
print(df)
df.to_excel("removed_Stop_Words.xlsx",engine='xlsxwriter' , index=False , header=True)






