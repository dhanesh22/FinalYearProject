import pandas as pd
import openpyxl
import xlsxwriter
import spacy
file_path = 'Organizations.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')

# ne = en_core_web_sm.load()
spcy = spacy.load(r"C:\Users\ANAND\AppData\Roaming\Python\Python39\site-packages\en_core_web_sm\en_core_web_sm-3.2.0")
def get_location(text):
  if type(text)==str and len(text)>10:
    sents = spcy(text)
    value = [str(ee) for ee in sents.ents if ee.label_ == 'GPE']
    value = list(set(value))
    if len(value)>0:
      return value
    else :
      return 'empty'
  else:
    return 'empty'
df["Locations"] = df["Long_Summary"].apply(lambda text: get_location(text))
df.to_excel("Locations.xlsx",engine='xlsxwriter' , index=False , header=True)