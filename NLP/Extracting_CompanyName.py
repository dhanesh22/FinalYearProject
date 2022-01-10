import pandas as pd
import openpyxl
import xlsxwriter
import spacy
file_path = 'removed_Stop_Words.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')

# ne = en_core_web_sm_abd.load()
spcy = spacy.load(r"C:\Users\ANAND\AppData\Roaming\Python\Python39\site-packages\en_core_web_sm\en_core_web_sm-3.2.0")
def get_organization(text):
    sents = spcy(text)
    value = [str(ee) for ee in sents.ents if ee.label_ == 'ORG']
    value=list(set(value))
    if len(value)>0:
      return value
    else :
      return 'empty'
df["Organization"] = df["Long_Summary"].apply(lambda text: get_organization(text))
print(df['Organization'])
df.to_excel("Organizations.xlsx",engine='xlsxwriter' , index=False , header=True)