import pandas as pd
import openpyxl
import xlsxwriter
import spacy
file_path = 'Locations.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')

# ne = en_core_web_sm.load()
spcy = spacy.load(r"C:\Users\ANAND\AppData\Roaming\Python\Python39\site-packages\en_core_web_sm\en_core_web_sm-3.2.0")
def get_money(text):
  if type(text)==str and len(text)>10:
    sents = spcy(text)
    value = [str(ee) for ee in sents.ents if ee.label_ == 'MONEY']
    if len(value)>0:
      return value
    else:
      return 'empty'
  else:
    return 'empty'
df["Money"] = df["Long_Summary"].apply(lambda text: get_money(text))
df.to_excel("Amount.xlsx",engine='xlsxwriter' , index=False , header=True)